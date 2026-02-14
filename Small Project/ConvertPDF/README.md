# PDF Tools - iLovePDF Style

A full-featured PDF toolkit built with Python Flask, inspired by iLovePDF.

## Features

| Tool | Description |
|------|-------------|
| **Convert to PDF** | Images, DOCX, TXT, HTML, Excel, PowerPoint → PDF |
| **Merge PDFs** | Combine multiple PDFs into one |
| **Split PDF** | Extract specific pages (e.g., 1,3,5-7) |
| **Compress PDF** | Reduce file size (3 quality levels) |
| **Rotate PDF** | Rotate pages 90°, 180°, 270° |
| **PDF to Image** | Convert PDF pages to JPG/PNG (requires Poppler) |

## Quick Start

### Prerequisites
- Python 3.9+
- pip

### Install & Run

```bash
cd ConvertPDF

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run
python app.py
```

Open: **http://localhost:5001**

### Docker

```bash
docker-compose up --build
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Web interface |
| GET | `/api/tools` | List available tools |
| POST | `/api/convert` | Convert file to PDF |
| POST | `/api/merge` | Merge multiple PDFs |
| POST | `/api/split` | Split PDF by pages |
| POST | `/api/compress` | Compress PDF |
| POST | `/api/rotate` | Rotate PDF pages |
| POST | `/api/pdf-to-image` | PDF to images (ZIP) |
| POST | `/api/pdf-info` | Get PDF page count |
| GET | `/health` | Health check |

## Tech Stack

- **Backend**: Python 3.11, Flask 3.0
- **PDF Tools**: PyPDF2, img2pdf, reportlab, pdf2image
- **Document Support**: python-docx, openpyxl, python-pptx
- **Frontend**: HTML, CSS, JavaScript

## License

MIT License
