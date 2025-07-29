#!/usr/bin/env python3
"""
Alternative PDF generation using available Python libraries
"""

import os
import subprocess
import sys
from datetime import datetime

def create_simple_pdf_content():
    """Create a simple text-based PDF content"""
    
    # Read the markdown file
    try:
        with open("RESTAURANT_MANAGEMENT_DOCUMENTATION.md", 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: RESTAURANT_MANAGEMENT_DOCUMENTATION.md not found")
        return None
    
    # Create a simple LaTeX-like formatted document
    pdf_content = f"""
DJANGO RESTAURANT MANAGEMENT SYSTEM
COMPREHENSIVE DOCUMENTATION
{'=' * 60}

Generated on: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
Version: 1.0.0

{'=' * 60}

{content}
"""
    
    return pdf_content

def try_pandoc_conversion():
    """Try to use pandoc if available"""
    try:
        # Check if pandoc is available
        result = subprocess.run(['which', 'pandoc'], capture_output=True, text=True)
        if result.returncode == 0:
            print("Pandoc found, attempting conversion...")
            
            # Convert markdown to PDF using pandoc
            cmd = [
                'pandoc',
                'RESTAURANT_MANAGEMENT_DOCUMENTATION.md',
                '-o', 'Restaurant_Management_Documentation.pdf',
                '--pdf-engine=pdflatex',
                '--toc',
                '--toc-depth=3',
                '--number-sections',
                '--highlight-style=github',
                '--geometry=margin=1in',
                '--variable=fontsize:11pt',
                '--variable=papersize:a4'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ PDF created successfully using Pandoc!")
                return True
            else:
                print(f"Pandoc conversion failed: {result.stderr}")
        
    except Exception as e:
        print(f"Pandoc not available or error: {e}")
    
    return False

def try_chromium_conversion():
    """Try to use chromium/chrome headless for PDF conversion"""
    browsers = ['chromium-browser', 'google-chrome', 'chromium', 'chrome']
    
    for browser in browsers:
        try:
            result = subprocess.run(['which', browser], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Found {browser}, attempting conversion...")
                
                # Create full file path
                html_file = os.path.abspath("Restaurant_Management_Documentation.html")
                pdf_file = os.path.abspath("Restaurant_Management_Documentation.pdf")
                
                cmd = [
                    browser,
                    '--headless',
                    '--disable-gpu',
                    '--print-to-pdf=' + pdf_file,
                    '--print-to-pdf-no-header',
                    '--run-all-compositor-stages-before-draw',
                    'file://' + html_file
                ]
                
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode == 0 and os.path.exists(pdf_file):
                    print(f"✅ PDF created successfully using {browser}!")
                    return True
                else:
                    print(f"{browser} conversion failed: {result.stderr}")
        
        except Exception as e:
            continue
    
    return False

def create_instructions_file():
    """Create detailed instructions for manual PDF conversion"""
    instructions = f"""
# PDF Generation Instructions

The documentation has been prepared in multiple formats for easy PDF conversion.

## Available Files:
1. `RESTAURANT_MANAGEMENT_DOCUMENTATION.md` - Original markdown
2. `Restaurant_Management_Documentation.html` - Styled HTML version
3. `Restaurant_Management_Documentation.txt` - Plain text version

## Method 1: Browser Print (Recommended)
1. Open `Restaurant_Management_Documentation.html` in any web browser
2. Press Ctrl+P (Windows/Linux) or Cmd+P (Mac)
3. In print dialog:
   - Destination: "Save as PDF"
   - Layout: Portrait
   - Paper size: A4 or Letter
   - Margins: Default
   - Options: ✓ Background graphics
   - More settings: ✓ Headers and footers (optional)
4. Click "Save" and name it `Restaurant_Management_Documentation.pdf`

## Method 2: Online Conversion
Upload the HTML file to these online converters:
- https://www.ilovepdf.com/html-to-pdf
- https://smallpdf.com/html-to-pdf
- https://www.sejda.com/html-to-pdf

## Method 3: Command Line Tools

### If you have wkhtmltopdf:
```bash
wkhtmltopdf --page-size A4 --margin-top 0.75in --margin-right 0.75in --margin-bottom 0.75in --margin-left 0.75in Restaurant_Management_Documentation.html Restaurant_Management_Documentation.pdf
```

### If you have pandoc:
```bash
pandoc RESTAURANT_MANAGEMENT_DOCUMENTATION.md -o Restaurant_Management_Documentation.pdf --pdf-engine=pdflatex --toc --number-sections
```

### If you have chromium/chrome:
```bash
chromium-browser --headless --disable-gpu --print-to-pdf=Restaurant_Management_Documentation.pdf file://$(pwd)/Restaurant_Management_Documentation.html
```

## Method 4: LibreOffice/OpenOffice
1. Open LibreOffice Writer
2. File → Open → Select `Restaurant_Management_Documentation.html`
3. File → Export as PDF
4. Configure PDF settings and save

## Quality Tips:
- Use A4 paper size for international compatibility
- Set margins to 0.75 inches for optimal readability
- Include page numbers and headers if desired
- Ensure background graphics are included for styled elements

Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
"""
    
    with open("PDF_Generation_Instructions.md", 'w', encoding='utf-8') as f:
        f.write(instructions)

def main():
    """Main function to attempt various PDF conversion methods"""
    print("🚀 Starting PDF generation process...")
    print("=" * 50)
    
    # First, ensure we have the necessary files
    if not os.path.exists("Restaurant_Management_Documentation.html"):
        print("❌ HTML file not found. Please run create_pdf.py first.")
        return
    
    # Try different conversion methods
    success = False
    
    print("\n1. Trying Pandoc conversion...")
    if try_pandoc_conversion():
        success = True
    
    if not success:
        print("\n2. Trying Chromium/Chrome headless conversion...")
        if try_chromium_conversion():
            success = True
    
    if not success:
        print("\n❌ Automatic PDF generation failed.")
        print("📋 Creating detailed manual conversion instructions...")
        create_instructions_file()
        print("\n✅ Manual conversion instructions created!")
        print("\n📁 Files available for manual PDF conversion:")
        print("   - Restaurant_Management_Documentation.html (for browser print)")
        print("   - Restaurant_Management_Documentation.txt (plain text)")
        print("   - PDF_Generation_Instructions.md (detailed instructions)")
        print("\n💡 Recommended: Open the HTML file in your browser and print to PDF")
    else:
        print(f"\n🎉 PDF file created: Restaurant_Management_Documentation.pdf")
        print(f"📄 File size: {os.path.getsize('Restaurant_Management_Documentation.pdf')} bytes")
    
    # List all created files
    print("\n📋 All generated files:")
    files = [
        "RESTAURANT_MANAGEMENT_DOCUMENTATION.md",
        "Restaurant_Management_Documentation.html", 
        "Restaurant_Management_Documentation.txt",
        "Restaurant_Management_Documentation.pdf",
        "PDF_Generation_Instructions.md",
        "README_PDF_Generation.md"
    ]
    
    for file in files:
        if os.path.exists(file):
            size = os.path.getsize(file)
            print(f"   ✅ {file} ({size:,} bytes)")
        else:
            print(f"   ❌ {file} (not created)")

if __name__ == "__main__":
    main()