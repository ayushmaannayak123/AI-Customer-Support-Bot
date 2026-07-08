# 🤖 AI Customer Support Automation System

An intelligent customer support assistant built with **LangGraph**, **LangChain**, **Ollama**, and **FAISS**. The system automates customer interactions by classifying queries, retrieving relevant information from a knowledge base using Retrieval-Augmented Generation (RAG), maintaining conversation history, and escalating sensitive requests for human approval.

---

## 🚀 Features

* **Intent Classification** – Automatically identifies the customer's request.
* **Department Routing** – Routes queries to the appropriate support agent (Sales, Billing, Technical Support, or Account Management).
* **Retrieval-Augmented Generation (RAG)** – Retrieves relevant information from company documents before generating responses.
* **Conversation Memory** – Stores previous conversations using SQLite for contextual interactions.
* **Human-in-the-Loop Approval** – Sensitive actions such as refunds or account closure require manual approval.
* **Supervisor Agent** – Validates and coordinates responses before they are returned to the customer.
* **Modular Multi-Agent Architecture** – Individual agents handle different business domains.
* **Local LLM Inference** – Powered by Ollama running the Qwen2.5:7B model.

---

## 🏗️ Architecture

The application follows an agent-based workflow built using LangGraph.

```
Customer Query
      │
      ▼
Intent Classification
      │
      ▼
Department Routing
      │
      ▼
RAG Knowledge Retrieval
      │
      ▼
Specialized Support Agent
      │
      ▼
Human Approval (if required)
      │
      ▼
Supervisor Agent
      │
      ▼
Conversation Memory (SQLite)
      │
      ▼
Final Response
```

A graphical representation of the workflow is available in **Workflow diagram.png**.

---

## 🛠️ Technology Stack

| Category             | Technologies                         |
| -------------------- | ------------------------------------ |
| Programming Language | Python                               |
| Agent Framework      | LangGraph, LangChain                 |
| Large Language Model | Ollama (Qwen2.5:7B)                  |
| Vector Search        | FAISS                                |
| Embeddings           | HuggingFace Embeddings               |
| Database             | SQLite                               |
| AI Technique         | Retrieval-Augmented Generation (RAG) |

---

## 📂 Project Structure

```
CustomerSupportBot/
│
├── agents/                 # Department-specific agents
│   ├── sales.py
│   ├── billing.py
│   ├── technical.py
│   └── account.py
│
├── documents/              # Knowledge base documents
├── database/               # SQLite database created at runtime
│
├── app.py                  # Entry point
├── graph.py                # LangGraph workflow
├── classifier.py           # Intent classification
├── rag.py                  # Retrieval-Augmented Generation
├── supervisor.py           # Supervisor agent
├── approval.py             # Human approval logic
├── memory.py               # Conversation memory
├── llm.py                  # LLM configuration
├── state.py                # Shared workflow state
│
├── requirements.txt
├── README.md
└── Workflow diagram.png
```

---

## 📚 Knowledge Base

The chatbot retrieves information from company documents before generating responses.

Example knowledge sources include:

* Pricing information
* Technical documentation
* Frequently Asked Questions
* Company policies

This allows the model to generate responses grounded in the available documentation rather than relying solely on the language model.

---

## 👤 Human Approval Workflow

Certain customer requests are considered high-risk and require manual approval before an AI-generated response is returned.

Examples include:

* Refund requests
* Subscription cancellation
* Account deletion
* Compensation requests
* Escalation to management

---

## 🧠 Conversation Memory

Customer conversations are stored using SQLite, allowing the assistant to recall previous interactions and maintain context across multiple queries.

Example:

**Customer**

> My application crashes whenever I upload a file.

Later:

> What was my previous support issue?

The chatbot retrieves the earlier conversation from the database and incorporates it into its response.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd CustomerSupportBot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment.

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download and install Ollama from:

https://ollama.com

Pull the required model:

```bash
ollama pull qwen2.5:7b
```

Start the Ollama server:

```bash
ollama serve
```

### 5. Configure environment variables

Create a `.env` file in the project root and add the required API keys or configuration variables if applicable.

### 6. Run the application

```bash
python app.py
```

---

## 💬 Sample Queries

### Sales

> What pricing plans do you offer?

### Technical Support

> My application crashes whenever I upload a file.

### Billing

> I would like a refund for my annual subscription.

### Account

> I forgot my password.

### Memory

> What was my previous support issue?

---

## 📈 Output

For each query, the system provides:

* Detected intent
* Assigned department
* Retrieved document context
* Approval status (when required)
* AI-generated response

---

## 🔮 Future Improvements

* Web-based interface
* Multi-user authentication
* CRM integration
* Email support
* Ticket generation
* Analytics dashboard
* Cloud deployment
* Containerization using Docker

## Used By: Pranav
