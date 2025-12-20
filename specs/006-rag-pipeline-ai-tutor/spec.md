# Feature Specification: RAG Pipeline and Student AI Tutor

**Feature Branch**: `006-rag-pipeline-ai-tutor`  
**Created**: 2025-12-19
**Status**: Draft  
**Input**: User description: "/sp.specify "RAG Pipeline and Student AI Tutor" --instructions "Architectural Alignment:
  1. Use Qdrant (Vector DB) and Gemini (text-embedding-004) for the indexing and retrieval pipeline.
  2. The logic must index all MDX content in 'docs/' with rich metadata (chapter, lesson, heading).
  3. Backend: Use Python (FastAPI) + OpenAI Agents SDK to build a 'TutorAgent' with a retrieval tool.
  4. Frontend: Create a custom, modern, floating Chat UI in the Docusaurus frontend (React/TypeScript).
  5. Success Criteria: The chat must support streaming (SSE), be context-aware of the current lesson, and follow our premium glassmorphic      
  theme.
  6. Workflow: Keep AI/Search logic in the backend; the frontend is purely for presentation and state." and there should be a feature to like  
  highlight the text to query it from the chatbot"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ask a question in the chat (Priority: P1)

A student reading the textbook has a question about the current content. They open the floating chat window, type their question, and receive a helpful, contextually relevant answer from the AI Tutor. The answer is streamed to the chat window so the user sees a response immediately.

**Why this priority**: This is the core functionality of the AI Tutor and provides the most immediate value to the user.

**Independent Test**: Can be tested by opening the chat on any textbook page, asking a question related to that page's content, and verifying that a relevant, streamed response is received.

**Acceptance Scenarios**:

1. **Given** a student is viewing a lesson page, **When** they open the chat and ask a question relevant to the text, **Then** the AI Tutor provides a streamed answer that directly addresses the question using information from the textbook.
2. **Given** the chat window is open, **When** the user asks a question, **Then** the user sees a "typing" or "processing" indicator while the answer is being generated.

---

### User Story 2 - Highlight text to ask a question (Priority: P2)

A student finds a specific term or concept in the textbook confusing. They highlight the text, and a small "Ask Tutor" button appears. Clicking this button opens the chat window with the highlighted text pre-filled in the input, allowing the student to quickly ask for clarification.

**Why this priority**: This feature makes the chatbot interaction more seamless and intuitive, directly connecting the user's point of confusion with the ability to ask a question.

**Independent Test**: Can be tested by highlighting any piece of text on a lesson page, clicking the contextual button, and verifying the chat opens with the correct text ready to be queried.

**Acceptance Scenarios**:

1. **Given** a student is viewing a lesson page, **When** they highlight a snippet of text, **Then** a small pop-up or button appears near the highlighted text.
2. **Given** the "Ask Tutor" button is visible, **When** the user clicks it, **Then** the chat interface opens and the highlighted text is populated in the chat input field.

---

### User Story 3 - Chat is aware of the current lesson (Priority: P3)

The AI Tutor's answers are more relevant because it knows which chapter and lesson the student is currently viewing. If the student asks a general question, the Tutor's response is biased towards the context of the current page.

**Why this priority**: Context-awareness improves the quality and relevance of the AI Tutor's responses, making it a more effective learning companion.

**Independent Test**: Can be tested by navigating to two different lessons, asking the same ambiguous question in the chat on each page, and verifying that the answers are tailored to the respective lesson's context.

**Acceptance Scenarios**:

1. **Given** a student is on "Chapter 1: Introduction", **When** they ask "What is the main goal?", **Then** the tutor's answer focuses on the goals of robotics as described in Chapter 1.
2. **Given** a student navigates to "Chapter 2: Reward Signals", **When** they ask the same question "What is the main goal?", **Then** the tutor's answer focuses on the goals of reward signals as described in Chapter 2.

### Edge Cases

- What happens if the user asks a question that is completely unrelated to the textbook content?
- How does the system handle very long highlighted text snippets?
- What happens if the backend service for the AI Tutor is unavailable?
- How does the chat UI behave on different screen sizes (mobile, tablet, desktop)?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST provide a floating chat interface accessible from all textbook pages.
- **FR-002**: The chat interface MUST allow users to input text questions.
- **FR-003**: The system MUST send the user's question and current page context (chapter, lesson) to a backend service.
- **FR-004**: The backend service MUST retrieve relevant content from a vector database (Qdrant) based on the user's query and context.
- **FR-005**: The backend service MUST use an AI agent (`TutorAgent`) to generate a response based on the retrieved content.
- **FR-006**: The system MUST stream the generated response to the frontend using Server-Sent Events (SSE).
- **FR-007**: The frontend MUST display the streamed response within the chat interface.
- **FR-008**: The system MUST provide a mechanism to highlight text within the MDX content.
- **FR-009**: The system MUST display a contextual menu or button when text is highlighted, allowing the user to query the highlighted text.
- **FR-010**: The chat interface MUST adhere to a glassmorphic visual theme.
- **FR-011**: The backend MUST have a process to index all MDX files from the `docs/` directory into the vector database.
- **FR-012**: The indexed documents MUST include metadata such as chapter, lesson, and the specific heading the content belongs to.
- **FR-013**: The Chat UI MUST render Markdown and LaTeX (using KaTeX or similar) for technical equations and formatting.
- **FR-014**: The AI Tutor's responses MUST include clickable citations or links back to the relevant source sections in the textbook.
- **FR-015**: The AI Tutor MUST strictly prioritize textbook content for its responses and clearly state when it is using general knowledge.

### Key Entities

- **Chat Message**: Represents a single message in the chat. Attributes: `content` (the text), `sender` (user or AI), `timestamp`.
- **Document Chunk**: Represents a piece of indexed content from the textbook. Attributes: `content` (text chunk), `metadata` (chapter, lesson, heading).
- **Chat Session**: Represents a user's entire conversation with the tutor. Attributes: `history` (list of Chat Messages), `context` (current lesson).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 95% of user queries related to the textbook content receive a relevant answer within 5 seconds.
- **SC-002**: The chat interface loads and becomes interactive in under 2 seconds on all textbook pages.
- **SC-003**: The system must support at least 50 concurrent chat users without a noticeable degradation in performance.
- **SC-004**: First-time users are able to successfully ask a question via highlighting text with a 90% success rate without instruction.
- **SC-005**: User satisfaction with the AI Tutor, measured by a simple "was this helpful?" feedback mechanism, achieves a score of 80% or higher.