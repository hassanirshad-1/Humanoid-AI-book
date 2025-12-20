from qdrant_client import QdrantClient, models
import os
import re
from pathlib import Path
from typing import List, Dict, Any
import uuid

from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.config import settings

def get_qdrant_client():
    return QdrantClient(url=settings.QDRANT_URL)

def get_embedding_model():
    if not settings.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable not set. Please set it to your Gemini API key.")
    return GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", google_api_key=settings.GEMINI_API_KEY)

def create_qdrant_collection():
    client = get_qdrant_client()
    # Delete collection if it already exists, for fresh indexing
    client.recreate_collection(
        collection_name=settings.QDRANT_COLLECTION_NAME,
        vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE),
    )

    client.create_payload_index(
        collection_name=settings.QDRANT_COLLECTION_NAME,
        field_name="chapter",
        field_schema="keyword",
    )

    client.create_payload_index(
        collection_name=settings.QDRANT_COLLECTION_NAME,
        field_name="lesson",
        field_schema="keyword",
    )
    client.create_payload_index(
        collection_name=settings.QDRANT_COLLECTION_NAME,
        field_name="heading_path",
        field_schema="keyword",
    )
    client.create_payload_index(
        collection_name=settings.QDRANT_COLLECTION_NAME,
        field_name="file_path",
        field_schema="keyword",
    )
    print(f"Collection '{settings.QDRANT_COLLECTION_NAME}' created with vector size 768 and payload indexes.")

def parse_mdx_content(file_path: Path) -> List[Dict[str, Any]]:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define headers to split on
    headers_to_split_on = [
        ("#", "header1"),
        ("##", "header2"),
    ]

    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    md_headers_splits = markdown_splitter.split_text(content)

    # Further chunking for each section
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=70,
        length_function=len,
        is_separator_regex=False,
    )

    chunks = []
    for split in md_headers_splits:
        # Extract metadata
        metadata = split.metadata.copy()
        
        # Extract chapter and lesson from file path
        relative_path = file_path.relative_to(settings.MDX_DOCS_PATH)
        # Normalize path to forward slashes for consistent regex matching
        rel_path_str = str(relative_path).replace("\\", "/")
        
        # chapter will be the first part of the path, e.g., 'chapter-01-intro'
        chapter_match = re.match(r"(chapter-\d{2}-[^/]+)", rel_path_str)
        if chapter_match:
            metadata["chapter"] = chapter_match.group(1)
        else:
            metadata["chapter"] = "unknown"

        # lesson will be the file name without extension
        metadata["lesson"] = file_path.stem
        metadata["file_path"] = str(relative_path)


        # Create heading_path from headers
        heading_path = []
        if "header1" in metadata:
            heading_path.append(metadata["header1"])
        if "header2" in metadata:
            heading_path.append(metadata["header2"])
        metadata["heading_path"] = " > ".join(heading_path) if heading_path else "top_level"

        # Split the text content of the markdown section
        section_chunks = text_splitter.split_text(split.page_content)
        for i, chunk_content in enumerate(section_chunks):
            chunk_metadata = {
                **metadata,
                "chunk_idx": i,
                "text_content": chunk_content, # Store original text content for retrieval
            }
            chunks.append({"page_content": chunk_content, "metadata": chunk_metadata})
    return chunks

def generate_embeddings(texts: List[str]) -> List[List[float]]:
    embedding_model = get_embedding_model()
    embeddings = embedding_model.embed_documents(texts)
    return embeddings

def index_all_mdx_content():
    client = get_qdrant_client()
    embedding_model = get_embedding_model() # Initialize once

    mdx_files = list(Path(settings.MDX_DOCS_PATH).rglob("*.mdx"))
    if not mdx_files:
        print(f"No .mdx files found in {settings.MDX_DOCS_PATH}. Exiting indexing.")
        return

    points = []
    for mdx_file in mdx_files:
        print(f"Processing {mdx_file}...")
        chunks = parse_mdx_content(mdx_file)
        
        if not chunks:
            print(f"No chunks generated for {mdx_file}. Skipping.")
            continue

        texts_to_embed = [chunk["page_content"] for chunk in chunks]
        embeddings = embedding_model.embed_documents(texts_to_embed)

        for i, chunk in enumerate(chunks):
            point_id = str(uuid.uuid4())
            points.append(
                models.PointStruct(
                    id=point_id,
                    vector=embeddings[i],
                    payload=chunk["metadata"],
                )
            )
        
        # Upload in batches to Qdrant
        if len(points) >= 100: # Batch size
            client.upsert(
                collection_name=settings.QDRANT_COLLECTION_NAME,
                wait=True,
                points=points,
            )
            points = []
    
    # Upload any remaining points
    if points:
        client.upsert(
            collection_name=settings.QDRANT_COLLECTION_NAME,
            wait=True,
            points=points,
        )
    print(f"Indexed {len(mdx_files)} MDX files and {len(points)} chunks into Qdrant collection '{settings.QDRANT_COLLECTION_NAME}'.")

if __name__ == "__main__":
    create_qdrant_collection()
    index_all_mdx_content()
    print("Indexing complete.")