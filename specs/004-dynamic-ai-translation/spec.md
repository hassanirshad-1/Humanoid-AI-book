# Feature Specification: Dynamic AI-Powered Content Translation

**Feature Branch**: `004-dynamic-ai-translation`  
**Created**: 2025-12-16  
**Status**: Draft  
**Input**: User description: "Dynamic AI-Powered Content Translation including page-level and selected text translation to Urdu using a local LLM."

## User Scenarios & Testing (mandatory)

### User Story 1 - Translate Entire Page to Urdu (Priority: P1)

A learner navigating the textbook wants to read an entire chapter or page in Urdu. They will use a clear UI control to switch the display language of the main content to Urdu.

**Why this priority**: This provides immediate value by making the core textbook content accessible in another language, a primary goal of the multilingual feature.

**Independent Test**: Can be fully tested by activating the language switch on any content page and verifying that the main textual content is displayed in Urdu, and then switching back to English.

**Acceptance Scenarios**:

1.  **Given** the user is viewing an English content page, **When** they click the "Translate to Urdu" button/option, **Then** the main textual content of the page is replaced with its Urdu translation.
2.  **Given** the user is viewing an Urdu translated page, **When** they click the "Show Original (English)" button/option, **Then** the main textual content of the page reverts to its original English version.
3.  **Given** the user is viewing an English content page, **When** they click the "Translate to Urdu" button/option, **Then** only the primary text content is translated, while UI elements (like navigation, footer, etc.) remain in English.

---

### User Story 2 - Translate Selected Text to Urdu (Priority: P2)

A learner is reading an English content page and encounters a specific phrase or sentence they don't fully understand. They want to get an on-demand Urdu translation of just that snippet without changing the entire page.

**Why this priority**: This enhances the reading experience by providing targeted assistance without disrupting the flow for the entire page, offering a more nuanced interaction.

**Independent Test**: Can be fully tested by selecting various text snippets on a page and verifying that a translation option appears and successfully displays the Urdu translation for only the selected text.

**Acceptance Scenarios**:

1.  **Given** the user is viewing an English content page, **When** they highlight a block of text (e.g., a sentence or paragraph), **Then** a context-sensitive UI element (e.g., a tooltip button) appears with an option to "Translate Selection".
    **Given** the user has highlighted text and a "Translate Selection" option is available, **When** they click "Translate Selection", **Then** an Urdu translation of the selected text appears in a non-disruptive tooltip near the selected text.
3.  **Given** the translation overlay for selected text is displayed, **When** the user dismisses the overlay (e.g., by clicking away), **Then** the overlay disappears, and the original text remains.

---

### Edge Cases

-   What happens when a page has no text content to translate? (e.g., a page with only images or code blocks) - The translation button should still function, but either return an empty translation or a message indicating no translatable content.
-   How does the system handle very long pages or very long selected texts? - The backend should be able to process requests up to a reasonable length limit (e.g., 5000 characters for a page, 500 for selection).
-   What happens if the local LLM is not running or is unreachable? - The frontend should display a user-friendly error message, and the translation request should fail gracefully.
-   What happens if the local LLM returns a poor quality translation or an error? - The frontend should display the raw response or an error message.

## Requirements (mandatory)

### Functional Requirements

-   **FR-001**: The system MUST provide a user interface control (e.g., a button or dropdown) in the Docusaurus frontend to trigger page-level translation to Urdu.
-   **FR-002**: When page-level translation is triggered, the frontend MUST send the complete textual content of the current page to the backend's `/api/translate` endpoint.
-   **FR-003**: The frontend MUST dynamically replace the original English text content on the page with the Urdu translation received from the backend.
-   **FR-004**: The system MUST provide a mechanism for the user to revert the page's translated content back to the original English.
-   **FR-005**: The user's chosen language for page-level translation (e.g., Urdu) MUST persist across different pages navigated within the textbook until explicitly changed or the session ends.
-   **FR-006**: The Docusaurus frontend MUST detect when a user highlights text (exceeding a minimal character count, e.g., 10 characters) and display a context-sensitive UI element ("Translate Selection" button/option).
-   **FR-005**: The Docusaurus frontend MUST detect when a user highlights text (exceeding a minimal character count, e.g., 10 characters) and display a context-sensitive UI element ("Translate Selection" button/option).
-   **FR-006**: When "Translate Selection" is activated, the frontend MUST send the selected text to the backend's `/api/translate` endpoint.
-   **FR-007**: The frontend MUST display the translated text for the selection in a non-disruptive tooltip near the selected text.
-   **FR-008**: The backend MUST expose a single `/api/translate` endpoint accessible by the frontend.
-   **FR-009**: The `/api/translate` endpoint MUST accept `POST` requests with a JSON body containing `text` (string) and `target_language` (string, e.g., "Urdu").
-   **FR-010**: The backend service MUST construct an appropriate prompt for the local LLM based on the input `text` and `target_language`.
-   **FR-011**: The backend service MUST make an HTTP request to the local LLM at `http://localhost:11434/v1` to obtain the translation.
-   **FR-012**: The backend service MUST parse the response from the local LLM and return the translated text (string) in a JSON response.
-   **FR-013**: The backend MUST handle cases where the local LLM is unreachable or returns an error, providing a clear error message to the frontend.

### Key Entities (if data involved)

-   **Translation Request**: Represents a request for translation.
    *   `text`: The source text to be translated (string).
    *   `target_language`: The language to translate into (string, e.g., "Urdu").
-   **Translation Response**: Represents the result of a translation.
    *   `translated_text`: The resulting translated text (string).
    *   `source_language` (optional): The detected source language (string).

## Success Criteria (mandatory)

### Measurable Outcomes

-   **SC-001**: Users can successfully translate an entire content page from English to Urdu within 5 seconds (from click to display) on a local development setup.
-   **SC-002**: Users can successfully translate selected text snippets (up to 500 characters) from English to Urdu within 3 seconds (from click to display) on a local development setup.
-   **SC-003**: The translation quality provided by the local LLM for Urdu content is sufficiently coherent and accurate for comprehension by 90% of test users.
-   **SC-004**: The system gracefully handles cases where the local LLM is unresponsive, providing an informative error message to the user within 5 seconds.