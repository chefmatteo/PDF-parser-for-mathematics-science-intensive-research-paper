from pathlib import Path
import pdfplumber
from ..utils.markdown_formatter import MarkdownFormatter
from ..utils.ocr_utils import OCRProcessor

class TextExtractor:
    def __init__(self):
        self.markdown_formatter = MarkdownFormatter()
        self.ocr_processor = OCRProcessor()
    
    def extract(self, pdf_path: Path) -> str:
        """Extract text content from PDF"""
        markdown_content = []
        
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if not text.strip():  # If page is scanned/image-based
                    text = self.ocr_processor.process_page(page)
                formatted_text = self.markdown_formatter.format(text)
                markdown_content.append(formatted_text)
                
        return "\n".join(markdown_content) 