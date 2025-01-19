# chefmatteo-PDF-parser-for-mathematics-science-intensive-research-paper

A Python application with a modern GUI that extracts and processes content from scientific PDF documents. Specifically designed to handle mathematical equations, citations, figures, and formatted text with special attention to academic paper structures.

## Features

### Content Extraction
- **Text Extraction**: 
  - Preserves paragraph formatting and structure
  - Handles multiple columns and complex layouts
  - OCR support for scanned documents

- **Image Processing**:
  - Extracts figures and diagrams
  - Maintains image quality
  - Supports common formats (JPG, PNG, BMP)
  - Basic image enhancement capabilities

- **Mathematical Content**:
  - LaTeX equation detection and extraction
  - Supports various equation environments (inline, display, align)
  - Preserves mathematical notation

- **Citation Handling**:
  - Extracts references and citations
  - Maintains citation order from the paper
  - Filters out page numbers and headers

### User Interface
- Modern Qt-based GUI
- Drag-and-drop PDF support
- Three-panel view:
  - Text content with preserved formatting
  - Extracted images gallery
  - References list
- Real-time processing feedback

## Installation

### Prerequisites
- Python 3.8 or higher
- Tesseract OCR (optional, for improved text extraction)

### Setup

1. Clone the repository:# PDF Parser for Mathematics & Science Research Papers

A Python application with a modern GUI that extracts and processes content from scientific PDF documents. Specifically designed to handle mathematical equations, citations, figures, and formatted text with special attention to academic paper structures.

## Features

### Content Extraction
- **Text Extraction**: 
  - Preserves paragraph formatting and structure
  - Handles multiple columns and complex layouts
  - OCR support for scanned documents

- **Image Processing**:
  - Extracts figures and diagrams
  - Maintains image quality
  - Supports common formats (JPG, PNG, BMP)
  - Basic image enhancement capabilities

- **Mathematical Content**:
  - LaTeX equation detection and extraction
  - Supports various equation environments (inline, display, align)
  - Preserves mathematical notation

- **Citation Handling**:
  - Extracts references and citations
  - Maintains citation order from the paper
  - Filters out page numbers and headers

### User Interface
- Modern Qt-based GUI
- Drag-and-drop PDF support
- Three-panel view:
  - Text content with preserved formatting
  - Extracted images gallery
  - References list
- Real-time processing feedback

## Installation

### Prerequisites
- Python 3.8 or higher
- Tesseract OCR (optional, for improved text extraction)

### Setup

1. Clone the repository:
2. Install dependencies:
3. Install Tesseract OCR (optional):
- **Windows**: Download from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
- **Linux**: `sudo apt-get install tesseract-ocr`
- **macOS**: `brew install tesseract`

## Usage

1. Run the application: run main.py
2. 2. Use the interface:
   - Drop a PDF file onto the application window
   - Or click to browse and select a file
   - View extracted content in the three panels:
     - Left: Formatted text
     - Middle: Extracted images
     - Right: Citations and references


## Dependencies

- **PDF Processing**:
  - `pdfplumber`: Text extraction
  - `PyMuPDF`: PDF parsing and image extraction

- **Image Processing**:
  - `opencv-python`: Image processing
  - `Pillow`: Image handling

- **OCR & Text**:
  - `pytesseract`: OCR capabilities
  - `regex`: Pattern matching

- **UI**:
  - `PyQt6`: Modern user interface

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

[@chefmatteo](https://github.com/chefmatteo)

## Acknowledgments

- Thanks to the developers of PyMuPDF, pdfplumber, and other open-source libraries used in this project
- Special thanks to the Tesseract OCR team for their excellent OCR engine
