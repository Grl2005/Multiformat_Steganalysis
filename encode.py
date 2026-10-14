from PIL import Image
import numpy as np
from docx import Document
from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

MARKER_START = "<<<HIDDEN_START>>>"
MARKER_END = "<<<HIDDEN_END>>>"

# ---------- IMAGE ----------
def encode_image(image, message):

    img = image.convert('RGB')
    data = np.array(img)

    message = MARKER_START + message + MARKER_END
    binary = ''.join(format(ord(c), '08b') for c in message)

    flat = data.flatten()

    for i in range(len(binary)):
        flat[i] = (flat[i] & 254) | int(binary[i])

    encoded = flat.reshape(data.shape)
    return Image.fromarray(encoded)


# ---------- TXT ----------
def encode_txt(file, message):

    content = file.read().decode("utf-8")
    hidden = content + "\n" + MARKER_START + message + MARKER_END
    return hidden


# ---------- DOCX ----------
def encode_docx(file, message):

    doc = Document(file)
    hidden = MARKER_START + message + MARKER_END
    doc.add_paragraph(hidden)

    return doc


# ---------- PDF ----------
def encode_pdf(file, message, output_name):

    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    hidden = MARKER_START + message + MARKER_END

    c = canvas.Canvas(output_name, pagesize=letter)

    y = 750
    for line in text.split("\n"):
        c.drawString(40, y, line[:100])
        y -= 15
        if y < 50:
            c.showPage()
            y = 750

    # invisible hidden message
    c.setFont("Helvetica", 1)
    c.drawString(1, 1, hidden)

    c.save()

    return output_name