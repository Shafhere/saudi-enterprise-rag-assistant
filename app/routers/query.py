from fastapi import APIRouter
from app.schemas import QueryRequest, QueryResponse
from app.services.rag_service import rag_service

router = APIRouter(prefix="/query", tags=["query"])

@router.post("/ask", response_model=QueryResponse)
def ask(req: QueryRequest):
    answer, sources = rag_service.answer(req.question)
    return QueryResponse(answer=answer, sources=sources)