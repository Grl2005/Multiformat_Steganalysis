# Multi-Format Steganalysis System

A Python-based application for encoding secret messages into digital files and detecting the presence of hidden data.

## Features

- Encode and detect hidden messages in PNG, JPG, and JPEG images.
- Support for TXT, DOCX, and PDF files.
- Least Significant Bit (LSB) encoding for images.
- Marker-based detection for text-based documents.
- Interactive interface built with Streamlit.

## Technologies Used

- Python
- Streamlit
- NumPy
- Pillow
- python-docx
- PyPDF2
- ReportLab

## Project Structure

```text
Multi-Format-Steganalysis/
├── steg.py
├── encode.py
├── detect.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Usage

1. Clone or download this repository.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   streamlit run steg.py
   ```

4. Select Encode or Detect.
5. Upload a supported file and follow the instructions on the interface.

## Limitations

The current implementation uses basic LSB encoding and predefined markers for detection. It is a demonstration project, not a comprehensive security scanner. It does not provide advanced encryption or reliable detection of every steganography technique.

## Academic Project

Developed as part of a Cryptography and Network Security laboratory project.