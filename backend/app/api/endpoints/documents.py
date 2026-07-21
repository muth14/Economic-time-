from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import List, Optional
from app.seed_data.seed_data import SAMPLE_DOCUMENTS
from app.services.document_processor import document_processor
from app.services.knowledge_graph import kg_service

router = APIRouter()

@router.get("/", response_model=List[dict])
def list_documents():
    return SAMPLE_DOCUMENTS

@router.post("/upload")
async def upload_document(file: UploadFile = File(...), file_type: Optional[str] = Form("PDF")):
    content_bytes = await file.read()
    try:
        content_str = content_bytes.decode("utf-8", errors="ignore")
    except Exception:
        content_str = f"Binary content for file {file.filename}"

    processed = document_processor.process_file_content(file.filename, content_str, file_type=file_type or "PDF")
    
    # Auto-update Knowledge Graph
    kg_service.add_document_nodes(processed)
    
    # Append to sample list in memory
    SAMPLE_DOCUMENTS.insert(0, processed)
    
    return {
        "message": f"Successfully processed and indexed document {file.filename}",
        "document": processed
    }

@router.get("/{doc_id}")
def get_document(doc_id: str):
    for d in SAMPLE_DOCUMENTS:
        if d["id"] == doc_id:
            return d
    raise HTTPException(status_code=404, detail="Document not found")
