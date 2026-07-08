# ABC Technologies - AI Customer Support Automation System

## Project Overview

This project is an AI-powered Customer Support Automation System developed using **LangGraph**, **LangChain**, **Ollama**, **FAISS**, and **SQLite**.

The system automates customer support by classifying customer queries, routing them to the appropriate support department, retrieving relevant information from company documents using Retrieval-Augmented Generation (RAG), maintaining customer conversation history, handling high-risk customer requests through human approval, and generating professional responses.

---

## Features

* Intent Classification
* Department-based Query Routing
* Retrieval-Augmented Generation (RAG)
* SQLite Conversation Memory
* Human-in-the-Loop Approval
* Supervisor Agent
* AI Response Generation using Ollama (Qwen2.5:7B)
* LangGraph Workflow

---

## Technologies Used

* Python
* LangGraph
* LangChain
* Ollama
* Qwen2.5:7B
* FAISS
* HuggingFace Embeddings
* SQLite

---

## Project Structure

```
CustomerSupportBot/

│
├── app.py
├── graph.py
├── state.py
├── classifier.py
├── rag.py
├── memory.py
├── approval.py
├── supervisor.py
├── llm.py
│
├── agents/
│     ├── sales.py
│     ├── technical.py
│     ├── billing.py
│     └── account.py
│
├── documents/
│     ├── pricing.txt
│     ├── technical.txt
│     ├── faq.txt
│     └── policy.txt
│
├── database/
│     └── memory.db
│
├── README.md
└── requirements.txt
```

---

## Workflow

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
Retrieve Relevant Documents (RAG)
        │
        ▼
Support Agent
        │
        ▼
Human Approval (if required)
        │
        ▼
Supervisor Agent
        │
        ▼
Store Conversation (SQLite)
        │
        ▼
Final Customer Response
```

---

## Knowledge Base Documents

The chatbot retrieves information from:

* Pricing Guide
* FAQ Document
* Technical Manual
* Company Policy

using Retrieval-Augmented Generation (RAG).

---

## Human Approval

The following requests require manual approval before a response is sent:

* Refund Requests
* Subscription Cancellation
* Account Closure
* Compensation Requests
* Escalation to Management

---

## Memory

Customer conversations are stored using SQLite.

Example:

Customer:

```
My application crashes whenever I upload a file.
```

Later:

```
What was my previous support issue?
```

The chatbot retrieves the previous issue from the SQLite database.

---

## Installation

Install all required Python packages:

```bash
pip install -r requirements.txt
```

Install Ollama:

https://ollama.com

Download the model:

```bash
ollama pull qwen2.5:7b
```

Start Ollama:

```bash
ollama serve
```

Run the chatbot:

```bash
python app.py
```

---

## Sample Queries

Sales

```
What are the pricing plans available for your software?
```

Account

```
I forgot my account password.
```

Technical Support

```
My application crashes whenever I upload a file.
```

Billing

```
I need a refund for my annual subscription.
```

Memory

```
What was my previous support issue?
```

---

## Output

The chatbot displays:

* Detected Department
* Retrieved Knowledge Base Context
* Approval Status
* Final AI-generated Response

---

## Future Improvements

* Web Interface
* Email Integration
* CRM Integration
* Ticket Generation
* Multi-user Authentication
