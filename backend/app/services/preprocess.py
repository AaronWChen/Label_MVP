import cv2
import numpy as np
from PIL import Image


def preprocess(image_bytes: bytes):
    file_bytes = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return Image.fromarray(gray)
