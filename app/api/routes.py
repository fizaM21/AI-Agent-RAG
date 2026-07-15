from pathlib import Path
import shutil

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.models.schemas import ChatRequest, ChatResponse
from app.agents.ai_agent import run_agent

from app.rag.loader import load_pdf
from app.rag.splitter import split_documents
from app.rag.embeddings import create_vector_store

router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.get("/")
def home():
    return {"message": "AI Agent RAG API is running"}


@router.get("/health")
def health():
    return {"status": "healthy"}


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        answer = run_agent(request.query)
        return ChatResponse(answer=answer)
    except Exception as e:
        print("ERROR:", repr(e))
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are allowed."
            )

        file_path = UPLOAD_DIR / file.filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        documents = load_pdf(str(file_path))
        chunks = split_documents(documents)
        create_vector_store(chunks)

        return {
            "message": "PDF uploaded and indexed successfully.",
            "filename": file.filename,
            "chunks": len(chunks)
        }

    except Exception as e:
        print("UPLOAD ERROR:", repr(e))
        raise HTTPException(status_code=500, detail=str(e))