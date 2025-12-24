# 🤖 Physical AI & Humanoid Robotics Textbook

> **An AI-Native, Interactive Learning Platform**
> *Learn Robotics with a Personal AI Tutor*

[![Built with Docusaurus](https://img.shields.io/badge/built%20with-docusaurus-3ecc5f.svg)](https://docusaurus.io)
[![FastAPI Backend](https://img.shields.io/badge/backend-FastAPI-009688.svg)](https://fastapi.tiangolo.com)
[![AI Powered](https://img.shields.io/badge/AI-Powered-blueviolet.svg)](https://openai.com)

## 📖 Overview

This project is a next-generation educational platform designed to teach **Physical AI and Humanoid Robotics**. Unlike traditional textbooks, this platform is **AI-Native**, meaning it integrates artificial intelligence directly into the reading experience to provide personalized tutoring, real-time translation, and interactive learning tools.

### 🌟 Key Features

-   **🤖 Personal AI Tutor**: A context-aware chatbot (RAG-powered) that answers questions based *specifically* on the textbook content you are reading.
-   **🇵🇰 Instant Translation**: Select any text to translate it into Urdu (or other languages) instantly, preserving the technical context.
-   **🧠 Adaptive Learning**: The AI tracks your skill level (Beginner to Expert) and operating system preference (Linux, Windows, macOS) to tailor explanations and code examples.
-   **🔍 Semantic Search**: Find concepts not just by keywords, but by meaning, using vector-based search.
-   **💬 Interactive Text Selection**: Highlight any text to immediately "Ask AI" or "Translate" without switching contexts.

## 🛠️ Tech Stack

### Frontend
-   **Framework**: [Docusaurus 3.6](https://docusaurus.io/) (React-based static site generator)
-   **Language**: TypeScript
-   **Styling**: CSS Modules, Infima
-   **State Management**: React Context API

### Backend
-   **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Python 3.13)
-   **Database**: PostgreSQL (User data), Qdrant (Vector Database for RAG)
-   **Authentication**: FastAPI Users (JWT, OAuth2)
-   **AI Engines**: Google Gemini / OpenAI (via custom agents)
-   **Package Manager**: `uv` (Ultra-fast Python package installer)

## 🚀 Getting Started

### Prerequisites
-   Node.js (v18+)
-   Python 3.13+
-   `uv` (Python package manager)

### 1. Clone the Repository
```bash
git clone https://github.com/hassanirshad-1/Robotics_book.git
cd Robotics_book
```

### 2. Backend Setup
The backend handles AI logic, authentication, and translation.

```bash
cd backend
# Create virtual environment and install dependencies
uv sync

# Create a .env file
cp .env.example .env
# Edit .env with your API Keys (GEMINI_API_KEY, DATABASE_URL, etc.)

# Run the server
uv run main.py
```
*Backend runs on `http://localhost:8000`*

### 3. Frontend Setup
The frontend displays the content and handles user interaction.

```bash
cd frontend
# Install dependencies
npm install

# Start the development server
npm start
```
*Frontend runs on `http://localhost:3000`*

## 🌐 Deployment

### Frontend (GitHub Pages)
The frontend is configured for automatic deployment to GitHub Pages.

1.  Update `docusaurus.config.ts` with your repository details.
2.  Build and Deploy:
    ```bash
    npm run build
    GIT_USER=<your-username> npm run deploy
    ```

### Backend
The backend can be deployed to any container-based hosting (Render, Railway, AWS).
-   **Docker**: A `Dockerfile` can be easily added to containerize the FastAPI app.
-   **Environment**: Ensure all `.env` variables are set in your production environment.

## 📂 Project Structure

```
Robotics_book/
├── backend/                # Python FastAPI Backend
│   ├── app/
│   │   ├── agents/         # AI Agent Logic (Tutor, Translator)
│   │   ├── routers/        # API Endpoints
│   │   └── models.py       # Database Schemas
│   └── tests/              # Pytest Backend Tests
├── frontend/               # Docusaurus Frontend
│   ├── docs/               # MDX Textbook Content (The Book!)
│   ├── src/
│   │   ├── components/     # React Components (ChatUI, Tooltips)
│   │   └── pages/          # Custom Pages (Register, Login)
│   └── docusaurus.config.ts
└── tests/                  # Integration & Content Tests
```

## 🤝 Contribution
Contributions are welcome! Please read `GEMINI.md` for the project constitution and coding conventions before submitting a Pull Request.

## 📄 License
This project is licensed under the MIT License.