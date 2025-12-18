"""
backend/app/services/translation.py

Service module containing the translation logic.
Refactored to use OpenAI Agents SDK for increased robustness.
"""
import asyncio
import json
import logging
from bs4 import BeautifulSoup, NavigableString
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner
from app.config import settings

# Configure logging
logger = logging.getLogger(__name__)

# --- System Prompts ---

SELECTION_SYSTEM_PROMPT = """You are an expert academic translator. 
Translate the given text from English to {target_language}.
RULES:
1. Return ONLY the translated text. No explanations, no "Here is the translation", no quotes.
2. Preserve original spacing and special characters.
3. If the input is code, math, or a variable name, return it EXACTLY as is.
4. Use natural, high-quality academic {target_language} suitable for a robotics textbook."""

BATCH_SYSTEM_PROMPT = """You are an expert academic translator. 
TASK: Translate the given JSON list of strings from English to {target_language}.
RULES:
1. Return ONLY a valid JSON list of strings.
2. DO NOT return a dictionary or object. Return a FLAT LIST of strings.
3. Maintain the EXACT same number of elements ({count}) as the input list.
4. Order MUST match the input list EXACTLY.
5. Translate naturally for a robotics textbook.
6. KEEP code, variables, and math notation exactly as they are.
7. Return ONLY the JSON list. No markdown blocks, no text content before or after."""

# --- Client and Agent Factory ---

def get_translation_client_and_model():
    """
    Returns an AsyncOpenAI client and model name based on the configured provider.
    """
    provider = settings.TRANSLATION_PROVIDER.lower()
    
    if provider == 'gemini':
        base_url = settings.GEMINI_BASE_URL
        api_key = settings.GEMINI_API_KEY
        model = settings.TRANSLATION_MODEL
    elif provider == 'ollama':
        base_url = settings.OLLAMA_BASE_URL
        api_key = settings.OLLAMA_API_KEY
        model = settings.TRANSLATION_MODEL
    else:
        # Fallback to ollama
        base_url = settings.OLLAMA_BASE_URL
        api_key = settings.OLLAMA_API_KEY
        model = settings.TRANSLATION_MODEL

    client = AsyncOpenAI(
        base_url=base_url,
        api_key=api_key,
        timeout=None # Let the LLM take its time for large batches
    )
    return client, model

def get_translation_agent(instructions: str):
    """
    Creates and returns an Agent using the OpenAI Agents SDK.
    """
    client, model_id = get_translation_client_and_model()
    model = OpenAIChatCompletionsModel(model=model_id, openai_client=client)
    return Agent(
        model=model,
        name="Translation Agent",
        instructions=instructions
    )

# --- Main Service Orchestrator ---

async def translate_text(text: str, target_language: str = "Urdu") -> str:
    """
    Parses HTML and translates text content using a recursive recovery loop to handle output truncation.
    """
    soup = BeautifulSoup(text, 'lxml')
    # Filter for meaningful text
    text_nodes = [
        node for node in soup.find_all(string=True) 
        if isinstance(node, NavigableString) and node.strip() and len(node.strip()) > 1
    ]
    exclude_tags = ['pre', 'code', 'script', 'style', 'kbd']
    
    valid_nodes = []
    for node in text_nodes:
        if not any(parent.name in exclude_tags for parent in node.parents):
            valid_nodes.append(node)

    print(f"DEBUG: Found {len(valid_nodes)} text nodes to translate.")

    if not valid_nodes:
        return str(soup)

    # Recursive Recovery Loop
    remaining_nodes = valid_nodes
    max_retries = 3
    retry_count = 0
    
    while remaining_nodes and retry_count < max_retries:
        texts_to_translate = [node.string for node in remaining_nodes]
        print(f"DEBUG: Attempt {retry_count + 1} - Translating {len(remaining_nodes)} remaining nodes.")
        
        try:
            translated_texts = await _translate_batch_agent(texts_to_translate, target_language)
            
            # Map translated texts back to nodes
            translated_count = 0
            for i, translated_val in enumerate(translated_texts):
                if i < len(remaining_nodes):
                    remaining_nodes[i].replace_with(translated_val)
                    translated_count += 1
            
            # Update remaining nodes for next iteration if partial
            if translated_count < len(remaining_nodes):
                print(f"WARNING: Partial translation. Got {translated_count}/{len(remaining_nodes)}. Retrying for rest.")
                remaining_nodes = remaining_nodes[translated_count:]
                retry_count += 1
            else:
                print(f"DEBUG: Successfully translated all {len(remaining_nodes)} nodes in this pass.")
                remaining_nodes = [] # Done!
                
        except Exception as e:
            print(f"ERROR: Translation attempt {retry_count + 1} failed: {e}")
            retry_count += 1
            # Wait a bit before retry to avoid rate limits if any
            await asyncio.sleep(1)
        
    if remaining_nodes:
        print(f"WARNING: Finished with {len(remaining_nodes)} nodes untranslated after {max_retries} attempts.")

    return str(soup)

# --- Agent-based Translation Function ---

async def _translate_batch_agent(texts: list[str], target_language: str) -> list[str]:
    """
    Translates a list of strings or a single string using the OpenAI Agents SDK.
    """
    try:
        # --- Optimization for Single Item (Text Selection) ---
        if len(texts) == 1:
            instructions = SELECTION_SYSTEM_PROMPT.format(target_language=target_language)
            agent = get_translation_agent(instructions)
            
            response = await Runner.run(agent, texts[0])
            content = response.final_output.strip()
            
            # Clean possible markdown
            if content.startswith("```"):
                lines = content.split('\n')
                if len(lines) >= 2:
                    content = '\n'.join(lines[1:-1])
            return [content.strip()]

        # --- Batch Translation Logic ---
        instructions = BATCH_SYSTEM_PROMPT.format(target_language=target_language, count=len(texts))
        agent = get_translation_agent(instructions)
        prompt_content = json.dumps(texts, ensure_ascii=False)
        
        response = await Runner.run(agent, prompt_content)
        content = response.final_output.strip()
        logger.debug(f"Agent Response (first 100 chars): {content[:100]}")

        # Clean up common model artifacts
        for tag in ["```json", "```"]:
            if content.startswith(tag):
                content = content[len(tag):]
            if content.endswith("```"):
                content = content[:-3]
        content = content.strip()

        # Robust JSON extraction: Find first '[' and last ']'
        start_idx = content.find('[')
        end_idx = content.rfind(']')
        
        parsed = None
        if start_idx != -1:
            # If no closing bracket, try to "auto-fix" it by taking the valid part
            if end_idx == -1 or end_idx < start_idx:
                logger.warning("JSON appears truncated (no closing bracket). Attempting auto-fix.")
                # Try to find the last valid comma-separated element
                temp_content = content[start_idx:]
                # Greedy match for list items: "item", or 'item',
                import re
                matches = re.findall(r'["\'](.*?)["\']\s*[,\]]', temp_content)
                if matches:
                    parsed = matches
                else:
                    # Last resort: just try appending a bracket
                    json_str = content[start_idx:] + '"]'
                    try: parsed = json.loads(json_str)
                    except: pass
            else:
                json_str = content[start_idx : end_idx + 1]
                try:
                    parsed = json.loads(json_str)
                except json.JSONDecodeError:
                    # Fallback: maybe it used single quotes or has trailing commas
                    try:
                        import ast
                        parsed = ast.literal_eval(json_str)
                    except:
                         pass

        # If we failed to find a list via brackets, try parsing the whole content as a dict
        if parsed is None:
            try:
                data = json.loads(content)
                if isinstance(data, list):
                    parsed = data
                elif isinstance(data, dict):
                    # Look for the first list in the dict values
                    for val in data.values():
                        if isinstance(val, list) and len(val) == len(texts):
                            parsed = val
                            break
                    # Fallback: if it returned { "original": "translation" }, take the values
                    if parsed is None and len(data) == len(texts):
                        parsed = list(data.values())
            except:
                pass

        if isinstance(parsed, list):
            # Return whatever we managed to parse (up to the requested length)
            # The caller (translate_text) will handle retrying for any missing items.
            if len(parsed) < len(texts):
                logger.warning(f"Returning partial translation: {len(parsed)}/{len(texts)}")
            return parsed[:len(texts)]
        
        raise ValueError(f"Could not extract a valid JSON list from agent response. Response started with: {content[:100]}")

    except Exception as e:
        logger.error(f"Agent translation error: {e}")
        raise e
