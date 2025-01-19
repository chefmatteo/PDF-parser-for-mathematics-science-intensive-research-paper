import re
from pathlib import Path
import pdfplumber

class CitationExtractor:
    """Class to handle citation extraction from PDF documents"""
    
    def __init__(self):
        self.reference_markers = [
            "References",
            "REFERENCES",
            "Bibliography",
            "BIBLIOGRAPHY",
            "Works Cited",
            "WORKS CITED"
        ]
    
    def extract(self, pdf_path: str) -> list:
        """
        Extract citations from PDF document
        
        Args:
            pdf_path: Path to PDF file
            
        Returns:
            List of citations with their order preserved
        """
        citations = []
        in_references = False
        
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if not text:
                    continue
                
                # Split text into lines
                lines = text.split('\n')
                
                for line in lines:
                    # Skip headers/footers (usually shorter and contain page numbers)
                    if len(line.strip()) < 10 or self._is_page_number(line):
                        continue
                    
                    # Check if we've reached the references section
                    if not in_references:
                        if any(marker in line for marker in self.reference_markers):
                            in_references = True
                            continue
                    
                    # If we're in the references section, collect citations
                    if in_references:
                        # Skip empty lines and section headers
                        if line.strip() and not any(marker in line for marker in self.reference_markers):
                            # Clean up the citation
                            citation = self._clean_citation(line)
                            if citation:
                                citations.append(citation)
        
        return citations
    
    def _is_page_number(self, text: str) -> bool:
        """Check if text is likely a page number"""
        # Remove common page number patterns
        text = text.strip()
        page_patterns = [
            r'^\d+$',  # Just numbers
            r'^Page \d+$',  # "Page" followed by numbers
            r'^\d+/\d+$',  # Format like 1/10
        ]
        return any(re.match(pattern, text) for pattern in page_patterns)
    
    def _clean_citation(self, text: str) -> str:
        """Clean up citation text"""
        # Remove leading numbers or bullets
        text = re.sub(r'^\s*\[?\d+\]?\s*\.?\s*', '', text)
        text = re.sub(r'^\s*[•●■]\s*', '', text)
        
        # Remove excessive whitespace
        text = ' '.join(text.split())
        
        return text.strip() 