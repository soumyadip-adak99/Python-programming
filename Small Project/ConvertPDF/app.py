import os
import uuid
import threading
import time
import atexit
from flask import Flask, render_template, request, jsonify, url_for, make_response
from werkzeug.utils import secure_filename
import img2pdf
from PIL import Image
from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key-here"
app.config["UPLOAD_FOLDER"] = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "uploads"
)
app.config["OUTPUT_FOLDER"] = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "outputs"
)
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024  # 50MB max file size

# Allowed extensions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "bmp", "txt", "docx", "html", "webp"}

# Ensure directories exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs(app.config["OUTPUT_FOLDER"], exist_ok=True)


# ============================================================
# Scheduler to clean up PDF files every 7 minutes
# ============================================================
class PDFCleanupScheduler:
    def __init__(self, output_folder, interval_minutes=7):
        self.output_folder = output_folder
        self.interval = interval_minutes * 60  # Convert to seconds
        self.running = False
        self.thread = None

    def cleanup_pdfs(self):
        """Delete all PDF files in the output folder"""
        try:
            if os.path.exists(self.output_folder):
                for filename in os.listdir(self.output_folder):
                    if filename.endswith(".pdf"):
                        file_path = os.path.join(self.output_folder, filename)
                        try:
                            os.remove(file_path)
                            print(f"[Scheduler] Deleted: {filename}")
                        except Exception as e:
                            print(f"[Scheduler] Error deleting {filename}: {e}")
                print(f"[Scheduler] Cleanup completed at {time.strftime('%H:%M:%S')}")
        except Exception as e:
            print(f"[Scheduler] Cleanup error: {e}")

    def run(self):
        """Background thread that runs cleanup every interval"""
        while self.running:
            time.sleep(self.interval)
            if self.running:
                self.cleanup_pdfs()

    def start(self):
        """Start the scheduler"""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.run, daemon=True)
            self.thread.start()
            print(f"[Scheduler] Started - will clean up PDFs every 7 minutes")

    def stop(self):
        """Stop the scheduler"""
        self.running = False
        print("[Scheduler] Stopped")


# Create and start the scheduler
pdf_scheduler = PDFCleanupScheduler(app.config["OUTPUT_FOLDER"], interval_minutes=7)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def get_file_extension(filename):
    return filename.rsplit(".", 1)[1].lower() if "." in filename else ""


def cleanup_all_pdfs():
    """Delete all PDF files in output folder"""
    output_folder = app.config["OUTPUT_FOLDER"]
    try:
        if os.path.exists(output_folder):
            for filename in os.listdir(output_folder):
                if filename.endswith(".pdf"):
                    file_path = os.path.join(output_folder, filename)
                    try:
                        os.remove(file_path)
                    except:
                        pass
    except:
        pass


def convert_image_to_pdf(image_path, output_path):
    """Convert image files to PDF"""
    try:
        with Image.open(image_path) as img:
            if img.mode in ("RGBA", "LA", "P"):
                rgb_img = Image.new("RGB", img.size, (255, 255, 255))
                if img.mode == "P":
                    img = img.convert("RGBA")
                rgb_img.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
                temp_path = image_path + "_temp.jpg"
                rgb_img.save(temp_path, "JPEG")
                image_path = temp_path

        with open(output_path, "wb") as f:
            f.write(img2pdf.convert(image_path))

        if image_path.endswith("_temp.jpg"):
            os.remove(image_path)

        return True
    except Exception as e:
        print(f"Error converting image: {e}")
        return False


def convert_text_to_pdf(text_path, output_path):
    """Convert text files to PDF"""
    try:
        with open(text_path, "r", encoding="utf-8", errors="ignore") as f:
            text_content = f.read()

        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72,
        )
        styles = getSampleStyleSheet()
        story = []

        paragraphs = text_content.split("\n")
        for para in paragraphs:
            if para.strip():
                story.append(Paragraph(para, styles["Normal"]))
            story.append(Spacer(1, 12))

        if not story:
            story.append(Paragraph("Empty document", styles["Normal"]))

        doc.build(story)
        return True
    except Exception as e:
        print(f"Error converting text: {e}")
        return False


def convert_docx_to_pdf(docx_path, output_path):
    """Convert DOCX files to PDF"""
    try:
        doc = Document(docx_path)
        pdf_doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72,
        )
        styles = getSampleStyleSheet()
        story = []

        for para in doc.paragraphs:
            if para.text.strip():
                story.append(Paragraph(para.text, styles["Normal"]))
            story.append(Spacer(1, 12))

        if not story:
            story.append(Paragraph("Empty document", styles["Normal"]))

        pdf_doc.build(story)
        return True
    except Exception as e:
        print(f"Error converting DOCX: {e}")
        return False


def convert_html_to_pdf(html_path, output_path):
    """Convert HTML files to PDF"""
    try:
        import re

        with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
            html_content = f.read()

        text_content = re.sub(r"<[^>]+>", "", html_content)
        text_content = re.sub(r"\s+", " ", text_content).strip()

        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72,
        )
        styles = getSampleStyleSheet()
        story = []

        words = text_content.split()
        chunks = [" ".join(words[i : i + 100]) for i in range(0, len(words), 100)]

        for chunk in chunks:
            if chunk.strip():
                story.append(Paragraph(chunk, styles["Normal"]))
                story.append(Spacer(1, 12))

        if not story:
            story.append(Paragraph("Empty document", styles["Normal"]))

        doc.build(story)
        return True
    except Exception as e:
        print(f"Error converting HTML: {e}")
        return False


def convert_to_pdf(input_path, output_path, file_extension):
    """Main conversion function"""
    converters = {
        "png": convert_image_to_pdf,
        "jpg": convert_image_to_pdf,
        "jpeg": convert_image_to_pdf,
        "gif": convert_image_to_pdf,
        "bmp": convert_image_to_pdf,
        "webp": convert_image_to_pdf,
        "txt": convert_text_to_pdf,
        "docx": convert_docx_to_pdf,
        "html": convert_html_to_pdf,
    }

    converter = converters.get(file_extension)
    if converter:
        return converter(input_path, output_path)
    return False


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        # Clean up all existing PDFs before creating new one
        cleanup_all_pdfs()

        # Generate unique filename
        original_filename = secure_filename(file.filename)
        file_extension = get_file_extension(original_filename)
        unique_id = str(uuid.uuid4())[:8]

        # Save uploaded file
        upload_path = os.path.join(
            app.config["UPLOAD_FOLDER"], f"{unique_id}_{original_filename}"
        )
        file.save(upload_path)

        # Generate output PDF path
        pdf_filename = f"{unique_id}_{original_filename.rsplit('.', 1)[0]}.pdf"
        output_path = os.path.join(app.config["OUTPUT_FOLDER"], pdf_filename)

        # Convert to PDF
        success = convert_to_pdf(upload_path, output_path, file_extension)

        # Clean up uploaded file
        try:
            os.remove(upload_path)
        except:
            pass

        if success:
            return jsonify(
                {
                    "success": True,
                    "message": "File converted successfully!",
                    "filename": pdf_filename,
                    "download_url": url_for("download_file", filename=pdf_filename),
                }
            )
        else:
            return jsonify({"error": "Failed to convert file"}), 500

    return jsonify({"error": "File type not allowed"}), 400


@app.route("/download/<filename>")
def download_file(filename):
    """Download and delete PDF file after sending"""
    safe_filename = secure_filename(filename)
    file_path = os.path.join(app.config["OUTPUT_FOLDER"], safe_filename)

    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    try:
        # Read file into memory
        with open(file_path, "rb") as f:
            pdf_data = f.read()

        # Delete file from server
        os.remove(file_path)

        # Create response with proper headers
        response = make_response(pdf_data)
        response.headers["Content-Type"] = "application/pdf"
        response.headers["Content-Disposition"] = (
            f'attachment; filename="{safe_filename}"'
        )
        response.headers["Content-Length"] = len(pdf_data)
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["X-Content-Type-Options"] = "nosniff"

        return response
    except Exception as e:
        print(f"Error downloading file: {e}")
        return jsonify({"error": "Download failed"}), 500


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


# Register cleanup on app shutdown
atexit.register(pdf_scheduler.stop)


if __name__ == "__main__":
    # Start the cleanup scheduler
    pdf_scheduler.start()
    app.run(host="0.0.0.0", port=5002, debug=True, use_reloader=False)
