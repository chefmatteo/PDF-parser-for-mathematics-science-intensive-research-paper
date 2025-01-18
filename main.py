from pathlib import Path
from src.parser import PDFParser

def main():
    # Initialize parser
    parser = PDFParser(model_provider="local")
    
    # Set up paths - using raw string with r prefix
    pdf_path = Path(r"C:\Users\matth\OneDrive\Desktop\s42979-021-00592-x.pdf")
    
    # OR using forward slashes
    # pdf_path = Path("C:/Users/matth/OneDrive/Desktop/s42979-021-00592-x.pdf")
    
    # OR using double backslashes
    # pdf_path = Path("C:\\Users\\matth\\OneDrive\\Desktop\\s42979-021-00592-x.pdf")
    
    output_dir = Path("extracted_content")
    output_dir.mkdir(exist_ok=True)
    
    # Process PDF
    result = parser.process_pdf(pdf_path, output_dir)
    
    # Save markdown content
    markdown_path = output_dir / "output.md"
    with open(markdown_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    # Print summary
    print(f"Processed PDF: {pdf_path}")
    print(f"Extracted {len(result['images'])} images")
    print(f"Found {len(result['equations'])} LaTeX equations")
    print(f"Output saved to: {output_dir}")

if __name__ == "__main__":
    main() 