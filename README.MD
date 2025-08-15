# AI-Powered Research Assistant

This project is an intelligent research assistant built with FastAPI, LangChain, and Gemini. It streamlines and accelerates the academic research process, enabling efficient knowledge discovery and management.

## Features

- **Separation of Concerns:** Modular design for ingestion, vector store, retrieval, agent orchestration, and API layer.
- **Vector Store:** Uses Chroma for embeddings, supports local and cloud-backed storage.
- **LLM Layer:** Configurable client adapter for Gemini and OpenAI.
- **Search Augmentation:** Integrates SERP API for fresh web search when the vector store lacks recent papers.
- **Orchestration:** Uses LangGraph to define parameterized flows (e.g., ingest → embed → index → summarize).
- **API:** FastAPI endpoint for question answering.

## Getting Started

### Prerequisites

- Python 3.10+
- [Poetry](https://python-poetry.org/) or `pip`
- Gemini and SERP API keys

### Installation

1. Clone the repository:
    ```sh
    git clone <repo-url>
    cd ResearchAgent
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv .venv
    .venv\Scripts\activate
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Copy `.env.example` to `.env` and fill in your API keys.

### Running the App

```sh
uvicorn app:app --reload --app-dir src