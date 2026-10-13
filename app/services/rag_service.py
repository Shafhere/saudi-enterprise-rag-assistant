import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_groq import ChatGroq
from rank_bm25 import BM25Okapi
from sentence_transformers import CrossEncoder
import numpy as np
from app.config import settings

load_dotenv()

EMBED_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
CROSS_ENCODER = "cross-encoder/ms-marco-MiniLM-L-6-v2"


class RAGService:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
        self.cross_encoder = CrossEncoder(CROSS_ENCODER)
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            print("⚠️  GROQ_API_KEY not found. Check your .env file.")
        self.llm = ChatGroq(
            model="openai/gpt-oss-120b",
            temperature=0.3,
            api_key=api_key,
            max_tokens=1024,
        )
        self.vectorstore = None
        self.bm25 = None
        self.texts = []

    def index_text(self, text: str):
        # Larger chunks for better context, bigger overlap for continuity
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1200,
            chunk_overlap=200,
            separators=["\n\n", "\n", ". ", " ", ""],
        )
        chunks = splitter.split_text(text)
        self.texts.extend(chunks)
        docs = [Document(page_content=c) for c in chunks]

        if self.vectorstore is None:
            self.vectorstore = Chroma.from_documents(
                documents=docs,
                embedding=self.embeddings,
                persist_directory=settings.chroma_dir,
            )
        else:
            self.vectorstore.add_documents(docs)
        self.vectorstore.persist()

        tokenized = [c.lower().split() for c in self.texts]
        self.bm25 = BM25Okapi(tokenized)

    def hybrid_search(self, query: str, k: int = 8):
        if self.vectorstore is None:
            return []
        vec_hits = [d.page_content for d in self.vectorstore.similarity_search(query, k=k)]
        tok = query.lower().split()
        scores = self.bm25.get_scores(tok)
        idx = np.argsort(scores)[-k:][::-1]
        bm25_hits = [self.texts[i] for i in idx]

        rrf = {}
        for rank, t in enumerate(vec_hits):
            rrf[t] = rrf.get(t, 0) + 1 / (60 + rank + 1)
        for rank, t in enumerate(bm25_hits):
            rrf[t] = rrf.get(t, 0) + 1 / (60 + rank + 1)
        candidates = sorted(rrf, key=lambda x: rrf[x], reverse=True)[:k]

        pairs = [[query, t] for t in candidates]
        ce_scores = self.cross_encoder.predict(pairs)
        reranked = [t for _, t in sorted(zip(ce_scores, candidates), reverse=True)]
        return reranked[:5]

    def answer(self, query: str):
        ctx = self.hybrid_search(query)
        if not ctx:
            return "No documents have been uploaded yet. Please upload a PDF first.", []

        context = "\n\n---\n\n".join(ctx)

        prompt = f"""You are Wathiqa, a professional Saudi enterprise document assistant.
Your job is to answer questions about uploaded business documents in a warm, clear, human-friendly way.

Guidelines:
- Write in complete, natural sentences — as if explaining to a busy executive.
- Be concise but thorough. 2–4 sentences is usually ideal.
- If the user asks for specific values (dates, amounts, IDs, names), always include them.
- If the context does not contain the answer, say exactly: "I could not find this information in the uploaded documents."
- Never invent facts. Only use what is in the context.
- If the text is Arabic, answer in Arabic. Otherwise, answer in English.

Context:
{context}

User question: {query}

Your answer:"""

        try:
            response = self.llm.invoke(prompt)
            return response.content.strip(), ctx
        except Exception as e:
            return f"LLM error: {type(e).__name__}: {e}", ctx


rag_service = RAGService()