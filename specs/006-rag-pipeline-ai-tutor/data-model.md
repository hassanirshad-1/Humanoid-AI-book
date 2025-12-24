# Data Model for RAG Pipeline and Student AI Tutor

This document defines the key data entities for the AI Tutor feature.

## 1. Chat Message

Represents a single message within a chat conversation.

- **`id`**: `string` (UUID) - Unique identifier for the message.
- **`session_id`**: `string` (UUID) - The chat session this message belongs to.
- **`sender`**: `string` - Indicates who sent the message. Can be `"user"` or `"ai"`.
- **`content`**: `string` - The text content of the message.
- **`timestamp`**: `datetime` - The time when the message was created.

**State Transitions**: A message is created and is immutable.

## 2. Document Chunk

Represents a piece of indexed content from the textbook stored in the vector database.

- **`id`**: `string` (UUID) - Unique identifier for the chunk in the vector DB.
- **`content`**: `string` - The text content of the chunk.
- **`metadata`**: `object` - A JSON object containing metadata about the chunk.
  - **`chapter`**: `string` - The chapter the content is from (e.g., "chapter-01-intro").
  - **`lesson`**: `string` - The lesson file name (e.g., "1.1-philosophy.mdx").
  - **`heading`**: `string` - The heading or sub-heading the content is under.
  - **`source_url`**: `string` - A direct link to the section in the textbook.

## 3. Chat Session

Represents a single, continuous conversation between a user and the AI Tutor.

- **`id`**: `string` (UUID) - Unique identifier for the session.
- **`user_id`**: `string` (Optional) - The ID of the authenticated user, if available.
- **`created_at`**: `datetime` - The time when the session was initiated.
- **`context`**: `object` - A JSON object containing the context of the chat.
  - **`current_url`**: `string` - The URL of the textbook page the user is currently on.
  - **`history`**: `array` - A list of `Chat Message` objects, representing the conversation history.

**Validation Rules**:
- A `Chat Session` can be initiated by any user, authenticated or anonymous.
- The `history` array should have a reasonable limit to prevent it from growing indefinitely.
