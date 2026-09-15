#!/usr/bin/env python3
"""
Script to convert PDFs to text files for better readability.
Requires: pip install pypdf2 or pip install pdfplumber
"""

import os
import sys
from pathlib import Path

def check_and_install_dependencies():
    """Check if required libraries are available, offer to install."""
    try:
        import PyPDF2
        return 'pypdf2'
    except ImportError:
        try:
            import pdfplumber
            return 'pdfplumber'
        except ImportError:
            print("No PDF library found. Installing PyPDF2...")
            os.system(f"{sys.executable} -m pip install PyPDF2 --quiet")
            try:
                import PyPDF2
                return 'pypdf2'
            except ImportError:
                print("Failed to install PyPDF2. Trying pdfplumber...")
                os.system(f"{sys.executable} -m pip install pdfplumber --quiet")
                try:
                    import pdfplumber
                    return 'pdfplumber'
                except ImportError:
                    print("ERROR: Could not install PDF libraries.")
                    print("Please run manually: pip install PyPDF2")
                    return None

def extract_text_pypdf2(pdf_path):
    """Extract text using PyPDF2."""
    import PyPDF2
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num, page in enumerate(pdf_reader.pages):
                text += f"\n--- Page {page_num + 1} ---\n"
                text += page.extract_text()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def extract_text_pdfplumber(pdf_path):
    """Extract text using pdfplumber (better quality)."""
    import pdfplumber
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                text += f"\n--- Page {page_num + 1} ---\n"
                page_text = page.extract_text()
                if page_text:
                    text += page_text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def convert_pdf_to_text(pdf_path, output_dir=None):
    """Convert a single PDF to text file."""
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        print(f"File not found: {pdf_path}")
        return False
    
    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True)
        output_path = output_dir / f"{pdf_path.stem}.txt"
    else:
        output_path = pdf_path.parent / f"{pdf_path.stem}.txt"
    
    library = check_and_install_dependencies()
    if not library:
        return False
    
    print(f"Converting {pdf_path.name}...")
    
    if library == 'pypdf2':
        text = extract_text_pypdf2(pdf_path)
    else:
        text = extract_text_pdfplumber(pdf_path)
    
    if text.strip():
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"  -> Saved to {output_path}")
        return True
    else:
        print(f"  -> Warning: No text extracted from {pdf_path.name}")
        return False

def main():
    """Main function to convert all PDFs in current directory."""
    current_dir = Path(__file__).parent
    pdf_files = list(current_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in current directory.")
        return
    
    print(f"Found {len(pdf_files)} PDF file(s).")
    print("Converting PDFs to text files...\n")
    
    # Create output directory
    txt_dir = current_dir / "pdf_texts"
    txt_dir.mkdir(exist_ok=True)
    
    success_count = 0
    for pdf_file in pdf_files:
        if convert_pdf_to_text(pdf_file, txt_dir):
            success_count += 1
    
    print(f"\nConversion complete: {success_count}/{len(pdf_files)} files converted.")
    print(f"Text files saved in: {txt_dir}")

if __name__ == "__main__":
    main()

