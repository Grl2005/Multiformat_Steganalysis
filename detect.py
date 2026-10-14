from PIL import Image
import numpy as np
from docx import Document
from PyPDF2 import PdfReader

MARKER_START = "<<<HIDDEN_START>>>"

# ---------- IMAGE ----------
def detect_image(image):

    img = Image.open(image).convert('RGB')
    data = np.array(img)

    flat = data.flatten()
    bits = flat & 1

    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        value = int(''.join(map(str, byte)), 2)
        chars.append(chr(value))

    message = ''.join(chars)

    if MARKER_START in message:
        return "Hidden Data Detected"
    else:
        return "No Hidden Data"


# ---------- TXT ----------
def detect_txt(file):

    content = file.read().decode("utf-8")

    if MARKER_START in content:
        return "Hidden Data Detected"
    else:
        return "No Hidden Data"


# ---------- DOCX ----------
def detect_docx(file):

    doc = Document(file)
    text = ""

    for para in doc.paragraphs:
        text += para.text

    if MARKER_START in text:
        return "Hidden Data Detected"
    else:
        return "No Hidden Data"


# ---------- PDF ----------
def detect_pdf(file):

    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    if MARKER_START in text:
        return "Hidden Data Detected"
    else:
        return "No Hidden Data"