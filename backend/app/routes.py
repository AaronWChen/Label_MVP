from fastapi import APIRouter, UploadFile, File
from .services.ocr import extract_text
from .services.extractor import extract_fields
from .services.verifier import verify

router = APIRouter()

@router.post("/verify")
async def verify_label(file: UploadFile = File(...)):
    image_bytes = await file.read()
    text = extract_text(image_bytes)
    fields = extract_fields(text)
    result = verify(fields, text)
    return {"raw_text": text, "fields": fields, "verification": result}
