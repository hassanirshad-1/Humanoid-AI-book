# Research & Decisions for RAG Pipeline and Student AI Tutor

## 1. Frontend Testing Framework

**Decision**: We will use **Jest** and **React Testing Library** for frontend testing.

**Rationale**:
- **Industry Standard**: Jest and React Testing Library are the de-facto standard for testing React applications, including those built with Docusaurus.
- **Docusaurus Integration**: Docusaurus is built on React, and these tools are well-supported and integrate seamlessly.
- **Component-Level Testing**: React Testing Library encourages good testing practices by focusing on testing component behavior from a user's perspective.
- **Community & Documentation**: Both projects have extensive documentation and a large community, making it easy to find help and resources.

**Alternatives considered**:
- **Cypress/Playwright**: These are excellent for end-to-end (E2E) testing, but for component-level unit and integration tests, Jest + React Testing Library is more suitable and faster. We may consider adding E2E tests with one of these tools later.
- **Mocha/Chai**: While viable, Jest provides an all-in-one solution with a test runner, assertion library, and mocking capabilities, which simplifies setup.

## 2. Frontend Testing Structure

**Decision**: Frontend tests will be co-located with the components they are testing, inside a `__tests__` directory.

**Rationale**:
- **Proximity**: Co-locating tests makes them easier to find and maintain. When a component is changed, the corresponding test is right next to it.
- **Clear Structure**: This is a common and well-understood convention in the React ecosystem.

**Example Structure**:
```
frontend/
└── src/
    └── components/
        └── Chat/
            ├── __tests__/
            │   ├── ChatUI.test.tsx
            │   └── index.test.tsx
            ├── index.tsx
            ├── ChatUI.tsx
            └── styles.module.css
```

## 3. Embedding Model Selection

**Decision**: We will use `gemini/text-embedding-004` as the text embedding model for the RAG pipeline.

**Rationale**:
- **User Requirement**: This was an explicit requirement in the initial feature specification.
- **State-of-the-Art**: `gemini/text-embedding-004` is a powerful and modern embedding model suitable for this task.
- **Architectural Alignment**: This decision is now documented and aligned with the project's technical direction for this feature.

**Implications**:
- The backend indexing and retrieval services must be implemented using the Google Generative AI SDK or a compatible library to generate embeddings with this model.
- The choice of embedding model is a critical architectural decision for the RAG system. If this model needs to be changed in the future, it will require re-indexing all content.
