from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import shutil, os
from app.database import get_db
from app.models import Document
from app.config import settings
from app.services.document_processor import extract_text, detect_language, classify_document
from app.services.pii_detector import detect_pii, mask_pii
from app.services.rag_service import rag_service

router = APIRouter(prefix="/documents", tags=["documents"])

@router.post("/upload")
async def upload(file: UploadFile = File(...), db: Session = Depends(get_db)):
    os.makedirs(settings.upload_dir, exist_ok=True)
    path = os.path.join(settings.upload_dir, file.filename)
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    raw_text = extract_text(path)
    language = detect_language(raw_text)
    doc_type = classify_document(raw_text)
    pii = detect_pii(raw_text)
    safe_text = mask_pii(raw_text)  # mask before indexing

    doc = Document(
        filename=file.filename,
        language=language,
        doc_type=doc_type,
        pii_count=sum(len(v) for v in pii.values()),
        preview=safe_text[:300],
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)

    rag_service.index_text(safe_text)  # index the MASKED text

    return {
        "id": doc.id,
        "filename": doc.filename,
        "language": language,
        "doc_type": doc_type,
        "pii_found": pii,
    }

@router.get("/")
def list_docs(db: Session = Depends(get_db)):
    return db.query(Document).order_by(Document.id.desc()).all()