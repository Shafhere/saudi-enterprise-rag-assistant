from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.database import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    language = Column(String, default="unknown")
    doc_type = Column(String, default="general")
    pii_count = Column(Integer, default=0)
    preview = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)