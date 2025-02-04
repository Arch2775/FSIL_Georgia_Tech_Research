import os
import pdfkit
import re


html_folder = r'C:\Users\archishman vb\OneDrive\Desktop\FSIL-RAG\html_files'
pdf_folder = r'C:\Users\archishman vb\OneDrive\Desktop\FSIL-RAG\pdf_files'

# Function to convert special characters to HTML entities
def convert_special_chars_to_entities(content):
    return re.sub(r'[^\x00-\x7F]+', lambda match: ''.join(f'&#{ord(char)};' for char in match.group()), content)

# Preprocess the HTML file
def preprocess_html(html_path):
    with open(html_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    
    content = convert_special_chars_to_entities(content)

    
    if '<meta charset="UTF-8">' not in content:
        content = content.replace('<head>', '<head><meta charset="UTF-8">', 1)

   
    with open(html_path, 'w', encoding='utf-8', errors='ignore') as file:
        file.write(content)


def convert_html_to_pdf(html_folder, pdf_folder):
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)
    
    html_files = [f for f in os.listdir(html_folder) if f.endswith('.html')]
    
    wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  
    
    if not os.path.isfile(wkhtmltopdf_path):
        raise FileNotFoundError(f'wkhtmltopdf executable not found at {wkhtmltopdf_path}')
    
    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
    options = {
        'load-error-handling': 'ignore',  # Ignore load errors
        'load-media-error-handling': 'ignore',  # Ignore media load errors
        'no-stop-slow-scripts': True,  # Do not stop slow scripts
        'disable-smart-shrinking': True,  # Disable smart shrinking
        'enable-local-file-access': None  # Allow access to local files
    }
    
    for html_file in html_files:
        html_path = os.path.join(html_folder, html_file)
        pdf_path = os.path.join(pdf_folder, html_file.replace('.html', '.pdf'))
        
        # Preprocess the HTML file to ensure correct encoding
        preprocess_html(html_path)
        
        try:
            pdfkit.from_file(html_path, pdf_path, configuration=config, options=options)
            print(f'Converted {html_file} to {pdf_path}')
        except OSError as e:
            print(f'Failed to convert {html_file}: {e}')

if __name__ == '__main__':
    convert_html_to_pdf(html_folder, pdf_folder)



