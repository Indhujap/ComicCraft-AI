from pathlib import Path
from app.config import EXPORTS_DIR

def save_pdf(story_data: dict, filename: str = "comic.pdf") -> Path:
    """
    Minimal PDF saver to fix ImportError.
    This will create a real PDF file in your exports folder.
    """
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas

    output_path = EXPORTS_DIR / filename
    c = canvas.Canvas(str(output_path), pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "ComicCraftAI - Generated Comic")

    c.setFont("Helvetica", 12)
    y = height - 100
    
    # Write whatever data comes from story
    text = str(story_data)[:2000] # first 2000 chars
    for line in text.split('\n'):
        if y < 50:
            c.showPage()
            y = height - 50
        c.drawString(50, y, line[:90])
        y -= 20

    c.save()
    return output_path
