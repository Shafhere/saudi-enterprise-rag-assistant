# Wathiqa — Saudi Document Intelligence Platform

Bilingual (Arabic/English) document Q&A with automatic PII masking, built for Saudi enterprise compliance (PDPL).

![Wathiqa Demo]()

## What it does
- Upload PDFs in Arabic or English
- Auto-detects language and document type (invoice, contract, identity, policy)
- Masks Saudi National IDs, IBANs, phone numbers, and emails before indexing
- Answers questions using Hybrid RAG with source-grounded responses

## Architecture

PDF → Extract text → Detect language → Mask PII → Chunk → Embed (ChromaDB)
↓
BM25 + Vector + RRF
↓
Cross-Encoder Rerank
↓
Groq Llama → Answer


## Tech Stack
Python · FastAPI · Streamlit · LangChain · ChromaDB · BM25 · RRF · Cross-Encoder · Groq · SQLAlchemy · Docker

## Quick Start
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
streamlit run dashboard/app.py

Docker
docker compose up --build

Demo

