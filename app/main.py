from fastapi import FastAPI
from app.database import Base, engine
from app.routers import documents, query

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Wathiqa — Saudi Document Intelligence")

app.include_router(documents.router)
app.include_router(query.router)

@app.get("/")
def root():
    return {"status": "ok", "service": "Saudi Enterprise RAG Assistance"}