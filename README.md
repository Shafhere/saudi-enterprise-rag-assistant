# Saudi Enterprise RAG Assistance

Bilingual (Arabic/English) document Q&A platform with automatic PII masking. Upload PDFs, ask questions, get source-grounded answers.

## Why this exists
Saudi enterprises handle thousands of Arabic/English documents daily. They can't search them, and PII exposure violates PDPL. This platform:
- Extracts text from PDFs
- Detects language (Arabic/English)
- Masks PII (Saudi ID, IBAN, phone, email) before indexing
- Classifies document type (invoice, contract, ID, policy)
- Answers questions using Hybrid RAG with citations

## Stack
FastAPI · Streamlit · ChromaDB · BM25 · RRF · Cross-Encoder · SQLAlchemy (SQLite) · Docker

## Run
```bash
docker compose up --build