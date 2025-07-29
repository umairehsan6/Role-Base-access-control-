#!/usr/bin/env python3
"""
Script to create a PDF-ready version of the Restaurant Management Documentation
"""

import os
from datetime import datetime

def read_markdown_file(filename):
    """Read the markdown file content"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return None

def markdown_to_text(markdown_content):
    """Convert markdown to plain text with basic formatting"""
    if not markdown_content:
        return ""
    
    lines = markdown_content.split('\n')
    formatted_lines = []
    
    for line in lines:
        # Handle headers
        if line.startswith('# '):
            formatted_lines.append('=' * 80)
            formatted_lines.append(line[2:].strip().upper())
            formatted_lines.append('=' * 80)
            formatted_lines.append('')
        elif line.startswith('## '):
            formatted_lines.append('-' * 60)
            formatted_lines.append(line[3:].strip())
            formatted_lines.append('-' * 60)
            formatted_lines.append('')
        elif line.startswith('### '):
            formatted_lines.append(f">>> {line[4:].strip()}")
            formatted_lines.append('')
        elif line.startswith('#### '):
            formatted_lines.append(f">> {line[5:].strip()}")
            formatted_lines.append('')
        # Handle code blocks
        elif line.startswith('```'):
            if 'python' in line or 'bash' in line or 'yaml' in line or 'dockerfile' in line or 'nginx' in line:
                formatted_lines.append('[CODE BLOCK START]')
            else:
                formatted_lines.append('[CODE BLOCK END]')
            formatted_lines.append('')
        # Handle lists
        elif line.startswith('- '):
            formatted_lines.append(f"  • {line[2:].strip()}")
        elif line.startswith('* '):
            formatted_lines.append(f"  • {line[2:].strip()}")
        # Handle bold text
        elif '**' in line:
            line = line.replace('**', '')
            formatted_lines.append(line)
        # Handle table separators
        elif line.startswith('|---'):
            formatted_lines.append('-' * 40)
        # Handle regular table rows
        elif line.startswith('|') and '|' in line[1:]:
            # Simple table formatting
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            formatted_line = ' | '.join(f"{cell:<15}" for cell in cells)
            formatted_lines.append(formatted_line)
        # Handle regular lines
        else:
            formatted_lines.append(line)
    
    return '\n'.join(formatted_lines)

def create_html_version(markdown_content):
    """Create an HTML version for better PDF conversion"""
    html_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Django Restaurant Management System - Documentation</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }
        
        h1 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            font-size: 2.5em;
        }
        
        h2 {
            color: #34495e;
            border-left: 4px solid #3498db;
            padding-left: 15px;
            margin-top: 40px;
            font-size: 1.8em;
        }
        
        h3 {
            color: #2980b9;
            margin-top: 30px;
            font-size: 1.4em;
        }
        
        h4 {
            color: #27ae60;
            margin-top: 25px;
            font-size: 1.2em;
        }
        
        pre {
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 5px;
            padding: 15px;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }
        
        code {
            background-color: #f1f3f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }
        
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        
        th {
            background-color: #3498db;
            color: white;
            font-weight: bold;
        }
        
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        
        ul, ol {
            padding-left: 30px;
        }
        
        li {
            margin-bottom: 5px;
        }
        
        .toc {
            background-color: #ecf0f1;
            padding: 20px;
            border-radius: 8px;
            margin: 30px 0;
        }
        
        .highlight {
            background-color: #fff3cd;
            padding: 15px;
            border-left: 4px solid #ffc107;
            margin: 20px 0;
        }
        
        .ascii-art {
            font-family: 'Courier New', monospace;
            background-color: #f8f9fa;
            padding: 15px;
            border: 1px solid #dee2e6;
            white-space: pre;
            overflow-x: auto;
        }
        
        @media print {
            body { font-size: 12px; }
            h1 { page-break-before: always; }
            h2 { page-break-before: auto; }
            pre, .ascii-art { page-break-inside: avoid; }
        }
    </style>
</head>
<body>
"""
    
    # Convert markdown to HTML (basic conversion)
    html_content = markdown_content
    
    # Replace markdown syntax with HTML
    html_content = html_content.replace('# ', '<h1>').replace('\n# ', '</h1>\n<h1>')
    html_content = html_content.replace('## ', '<h2>').replace('\n## ', '</h2>\n<h2>')
    html_content = html_content.replace('### ', '<h3>').replace('\n### ', '</h3>\n<h3>')
    html_content = html_content.replace('#### ', '<h4>').replace('\n#### ', '</h4>\n<h4>')
    
    # Handle code blocks
    html_content = html_content.replace('```python', '<pre><code class="python">')
    html_content = html_content.replace('```bash', '<pre><code class="bash">')
    html_content = html_content.replace('```yaml', '<pre><code class="yaml">')
    html_content = html_content.replace('```dockerfile', '<pre><code class="dockerfile">')
    html_content = html_content.replace('```nginx', '<pre><code class="nginx">')
    html_content = html_content.replace('```txt', '<pre><code class="txt">')
    html_content = html_content.replace('```', '</code></pre>')
    
    # Handle ASCII art sections
    import re
    ascii_pattern = r'```\n([\s\S]*?)\n```'
    html_content = re.sub(ascii_pattern, r'<div class="ascii-art">\1</div>', html_content)
    
    # Handle bold text
    html_content = html_content.replace('**', '<strong>', 1).replace('**', '</strong>', 1)
    
    # Handle inline code
    html_content = re.sub(r'`([^`]+)`', r'<code>\1</code>', html_content)
    
    # Handle line breaks
    html_content = html_content.replace('\n\n', '</p>\n<p>')
    html_content = '<p>' + html_content + '</p>'
    
    # Close any unclosed headers
    html_content = html_content.replace('<h1>', '<h1>').replace('\n<h1>', '</h1>\n<h1>')
    html_content = html_content.replace('<h2>', '<h2>').replace('\n<h2>', '</h2>\n<h2>')
    html_content = html_content.replace('<h3>', '<h3>').replace('\n<h3>', '</h3>\n<h3>')
    html_content = html_content.replace('<h4>', '<h4>').replace('\n<h4>', '</h4>\n<h4>')
    
    # Add metadata
    metadata = f"""
    <div style="text-align: center; margin-bottom: 40px; border-bottom: 2px solid #3498db; padding-bottom: 20px;">
        <h1 style="margin: 0; color: #2c3e50;">Django Restaurant Management System</h1>
        <h2 style="margin: 10px 0; color: #7f8c8d; font-weight: normal;">Comprehensive Documentation</h2>
        <p style="margin: 5px 0; color: #95a5a6;">Generated on: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
        <p style="margin: 5px 0; color: #95a5a6;">Version: 1.0.0</p>
    </div>
    """
    
    return html_template + metadata + html_content + "\n</body>\n</html>"

def main():
    """Main function to convert markdown to PDF-ready formats"""
    input_file = "RESTAURANT_MANAGEMENT_DOCUMENTATION.md"
    
    print("Reading documentation file...")
    markdown_content = read_markdown_file(input_file)
    
    if not markdown_content:
        print("Failed to read the documentation file.")
        return
    
    print("Creating formatted text version...")
    text_content = markdown_to_text(markdown_content)
    
    # Write text version
    with open("Restaurant_Management_Documentation.txt", 'w', encoding='utf-8') as f:
        f.write("DJANGO RESTAURANT MANAGEMENT SYSTEM - COMPREHENSIVE DOCUMENTATION\n")
        f.write("=" * 80 + "\n")
        f.write(f"Generated on: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}\n")
        f.write("Version: 1.0.0\n")
        f.write("=" * 80 + "\n\n")
        f.write(text_content)
    
    print("Creating HTML version...")
    html_content = create_html_version(markdown_content)
    
    # Write HTML version
    with open("Restaurant_Management_Documentation.html", 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("\nFiles created successfully:")
    print("1. Restaurant_Management_Documentation.txt - Plain text version")
    print("2. Restaurant_Management_Documentation.html - HTML version (can be printed to PDF)")
    print("\nTo convert HTML to PDF:")
    print("1. Open Restaurant_Management_Documentation.html in your browser")
    print("2. Use Ctrl+P (or Cmd+P on Mac) to print")
    print("3. Select 'Save as PDF' as the destination")
    print("4. Choose appropriate settings (A4, margins, etc.)")
    
    # Also create a simple README for the PDF conversion
    readme_content = """# Restaurant Management Documentation

This directory contains comprehensive documentation for the Django Restaurant Management System.

## Files:
- `RESTAURANT_MANAGEMENT_DOCUMENTATION.md` - Original markdown source
- `Restaurant_Management_Documentation.html` - HTML version optimized for PDF conversion
- `Restaurant_Management_Documentation.txt` - Plain text version
- `create_pdf.py` - Script used to generate these files

## Converting to PDF:

### Method 1: Browser Print
1. Open `Restaurant_Management_Documentation.html` in any modern web browser
2. Press Ctrl+P (Windows/Linux) or Cmd+P (Mac)
3. Select "Save as PDF" or "Print to PDF"
4. Adjust settings:
   - Paper size: A4 or Letter
   - Margins: Normal
   - Include background graphics: Yes
5. Save as `Restaurant_Management_Documentation.pdf`

### Method 2: Online Converter
1. Upload `Restaurant_Management_Documentation.html` to online converters like:
   - HTML to PDF converter
   - SmallPDF
   - ILovePDF
2. Download the generated PDF

### Method 3: Command Line (if wkhtmltopdf is available)
```bash
wkhtmltopdf Restaurant_Management_Documentation.html Restaurant_Management_Documentation.pdf
```

## Documentation Contents:
- Complete system overview and architecture
- Detailed feature specifications
- Database models and API documentation
- Installation and deployment guides
- Security and best practices
- Future enhancement roadmap

Generated on: """ + datetime.now().strftime('%B %d, %Y at %I:%M %p') + """
Version: 1.0.0
"""
    
    with open("README_PDF_Generation.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("5. README_PDF_Generation.md - Instructions for PDF conversion")

if __name__ == "__main__":
    main()