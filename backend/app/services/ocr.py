import pytesseract
from .preprocess import preprocess


def extract_text(image_bytes: bytes) -> str:
    image = preprocess(image_bytes)
    return pytesseract.image_to_string(image)
