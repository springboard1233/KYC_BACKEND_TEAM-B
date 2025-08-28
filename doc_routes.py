from fastapi import APIRouter, UploadFile, File
import shutil, os

router = APIRouter()

UPLOAD_DIR = "data/"

@router.post("/upload-doc")
async def upload_document(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "message": "File uploaded successfully"}
