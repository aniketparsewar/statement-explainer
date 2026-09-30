"""Extract text from a PDF statement."""
import pymupdf


def extract_text(pdf_path: str) -> tuple[str, int]:
    """Return (full_text, page_count) for the PDF at pdf_path."""
    doc = pymupdf.open(pdf_path)
    try:
        pages = [page.get_text() for page in doc]
    finally:
        doc.close()
    return "\n\n".join(pages), len(pages)
