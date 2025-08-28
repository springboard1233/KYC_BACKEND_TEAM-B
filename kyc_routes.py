from fastapi import APIRouter
from src.ocr_reader import extract_text

router = APIRouter()

@router.get("/extract-data/{filename}")
def extract_data(filename: str):
    path = f"data/{filename}"
    text = extract_text(path)
    return {"filename": filename, "extracted_text": text}
