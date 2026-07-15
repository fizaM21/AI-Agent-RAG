# 🤖 AI Agent with Retrieval-Augmented Generation (RAG)

> An intelligent AI agent built with **Python, FastAPI, LangChain, and LLMs** that combines Retrieval-Augmented Generation (RAG), structured tool calling, and external API integrations to deliver accurate, context-aware responses.

---

## 🚀 Overview

This project demonstrates how to build a production-style AI agent capable of:

* Understanding natural language queries
* Retrieving relevant knowledge from uploaded documents using RAG
* Calling external tools dynamically based on user intent
* Performing multi-step reasoning
* Exposing all functionality through a FastAPI REST API

The architecture is modular, scalable, and designed using modern GenAI development practices.

---

## ✨ Features

* 📄 Retrieval-Augmented Generation (RAG)
* 🧠 Context-aware question answering
* 🤖 LangChain Agent with structured tool calling
* 🌦️ Live Weather API integration
* 📚 Wikipedia search tool
* 🧮 Calculator tool
* 💬 Follow-up conversation support
* ⚡ FastAPI REST API
* 📂 PDF document ingestion
* 🔍 Semantic search with embeddings
* 🛠️ Modular project architecture
* 🔐 Secure API key management using `.env`

---

## 🛠️ Tech Stack

| Category        | Technologies                          |
| --------------- | ------------------------------------- |
| Language        | Python                                |
| Backend         | FastAPI                               |
| AI Framework    | LangChain                             |
| RAG             | FAISS + Sentence Transformers         |
| LLM             | Groq / OpenAI / Gemini (configurable) |
| APIs            | OpenWeather API, Wikipedia API        |
| Data Validation | Pydantic                              |
| Server          | Uvicorn                               |
| Version Control | Git & GitHub                          |

---

## 🏗️ Project Architecture

```text
                User Query
                     │
                     ▼
              FastAPI Endpoint
                     │
                     ▼
              LangChain Agent
                     │
      ┌──────────────┼──────────────┐
      │              │              │
      ▼              ▼              ▼
   Calculator     Weather API   Wikipedia
      │              │              │
      └──────────────┼──────────────┘
                     ▼
              RAG Retrieval Engine
                     │
             Vector Search (FAISS)
                     │
             Embedded PDF Documents
                     │
                     ▼
              Final AI Response
```

---

## 📁 Project Structure

```text
AI-Agent-RAG/
│
├── app/
│   ├── agents/
│   ├── rag/
│   ├── routes/
│   ├── prompts/
│   ├── tools/
│   ├── config.py
│   └── main.py
│
├── documents/
├── uploads/
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/AI-Agent-RAG.git
```

Navigate into the project

```bash
cd AI-Agent-RAG
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_key
GROQ_API_KEY=your_key
WEATHER_API_KEY=your_key
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 📌 Example Request

```http
POST /chat
```

```json
{
    "message": "What's the weather in Bangalore today?"
}
```

---

## 📈 Future Enhancements

* Conversation memory
* Multi-agent workflows
* Qdrant / Pinecone vector database
* Authentication & authorization
* Docker containerization
* CI/CD pipeline
* Cloud deployment (AWS/GCP/Azure)
* Streaming responses
* Multi-document retrieval

---

## 🎯 Skills Demonstrated

* Generative AI
* Retrieval-Augmented Generation (RAG)
* LangChain
* Prompt Engineering
* Tool Calling
* API Integration
* FastAPI Development
* REST APIs
* Semantic Search
* Vector Embeddings
* Python Backend Development
* Git & GitHub

---

## 🤝 Contributing

Contributions, feature requests, and suggestions are welcome. Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.
