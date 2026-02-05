# PDF Converter - Python Flask

A simple file to PDF converter built with Python Flask.

## Features

- **File Conversion**: Convert images (PNG, JPG, GIF, BMP, WebP), text files, DOCX, and HTML to PDF
- **Drag & Drop Upload**: User-friendly interface with drag-and-drop support
- **Automatic Cleanup**: PDFs are automatically deleted every 7 minutes
- **Download & Delete**: Files are automatically removed from server after download
- **50MB File Limit**: Supports files up to 50MB

## Tech Stack

- **Backend**: Python 3.11, Flask 3.0
- **PDF Generation**: img2pdf, Pillow, python-docx, reportlab
- **Frontend**: HTML, CSS, JavaScript (Jinja2)
- **Production Server**: Gunicorn

## Quick Start

### Prerequisites

- Python 3.9+
- pip

### Run Locally

```bash
# Clone and navigate to project
cd ConvertPDF

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

The application will be available at `http://localhost:5002`

### Docker

```bash
# Build and run with Docker Compose
docker-compose up --build
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Web interface |
| POST | `/upload` | Upload and convert file |
| GET | `/download/<filename>` | Download PDF |
| GET | `/health` | Health check |

## Project Structure

```
ConvertPDF/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend template
├── static/
│   └── style.css       # Styling
├── uploads/            # Temporary upload folder
├── outputs/            # Generated PDFs
├── Dockerfile
└── docker-compose.yml
```

## License

MIT License
