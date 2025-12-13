# ADR-001: Content Authoring and Presentation Stack

- **Status:** Accepted
- **Date:** 2025-12-11
- **Feature:** 001-intro-robotics
- **Context:** The project requires a robust system for authoring and presenting an educational textbook that integrates formatted text, images, code snippets, and interactive components. The chosen platform needs to provide a smooth authoring experience, be easily maintainable, and be structured in a way that is optimal for future AI-driven features like RAG-based chatbots.

## Decision

The project will use the following stack for content authoring and presentation:
- **Content Format**: MDX (Markdown with JSX), allowing for the embedding of interactive React components directly within the content.
- **Presentation Framework**: Docusaurus, a static site generator optimized for documentation and educational content.
- **Content Structure**: Each lesson will be an atomic `.mdx` file. This modular structure is intended to improve maintainability and facilitate more precise RAG retrieval for AI agents.

## Consequences

### Positive

- **Rich Feature Set**: Docusaurus provides a "batteries-included" solution with theming, versioning, search, and navigation, reducing development overhead.
- **Interactive Content**: MDX enables a rich, interactive user experience by allowing React components to be used directly in the markdown.
- **RAG Optimization**: The atomic file structure per lesson allows AI agents to retrieve more focused and relevant context.
- **Strong Ecosystem**: Docusaurus has a large and active community.

### Negative

- **Ecosystem Lock-in**: The project becomes dependent on the Docusaurus ecosystem, its release cycle, and its limitations.
- **Customization Complexity**: While themeable, complex customizations that go against Docusaurus conventions can be difficult to implement and maintain.

## Alternatives Considered

- **Alternative A: Jupyter Book**
  - **Description**: A documentation generator that builds books from Jupyter Notebooks.
  - **Why Rejected**: While excellent for notebook-centric content, it is less suited for a general-purpose textbook structure that mixes prose and code examples outside of a notebook format.

- **Alternative B: Sphinx**
  - **Description**: A powerful and mature documentation generator, primarily used in the Python community.
  - **Why Rejected**: It has a steeper learning curve and its default themes are generally considered less modern than Docusaurus. The authoring experience in reStructuredText can be less intuitive than Markdown/MDX.

- **Alternative C: Custom Next.js/React Site**
  - **Description**: Building a custom frontend from scratch.
  - **Why Rejected**: This approach offers maximum flexibility but at the cost of significantly higher development effort. Core documentation features like navigation, search, and versioning would need to be built from the ground up.

## References

- **Implementation Plan**: `specs/001-intro-robotics/plan.md`
