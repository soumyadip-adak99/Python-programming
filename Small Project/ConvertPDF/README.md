# Flask PDF Converter

A modern Flask web application to convert various file types to PDF format.

## Features

- 🖼️ Convert images (PNG, JPG, JPEG, GIF, BMP, WebP) to PDF
- 📝 Convert text files to PDF
- 📄 Convert Word documents (DOCX) to PDF
- 🌐 Convert HTML files to PDF
- 🎨 Modern dark theme UI with glassmorphism effects
- 🐳 Docker support for easy deployment

## Quick Start

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Visit `http://localhost:5000` in your browser.

### Docker

```bash
# Build and run with Docker Compose
docker-compose up --build

# Or build manually
docker build -t pdf-converter .
docker run -p 5000:5000 pdf-converter
```

## Project Structure

```
ConvertPDF/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose config
├── .dockerignore         # Docker ignore file
├── templates/
│   └── index.html        # Frontend HTML
├── static/
│   └── style.css         # CSS styles
├── uploads/              # Temporary upload folder
└── outputs/              # Generated PDF files
```

## Supported Formats

| Input Format | Output |
|--------------|--------|
| PNG, JPG, JPEG, GIF, BMP, WebP | PDF |
| TXT | PDF |
| DOCX | PDF |
| HTML | PDF |

## License

MIT License
