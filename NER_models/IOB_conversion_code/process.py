import os
import re
from bs4 import BeautifulSoup

def convert_html_to_iob(html_file):
    """
    Converts an HTML file to IOB format.

    Args:
        html_file: Path to the HTML file.

    Returns:
        A list of strings, where each string represents a line in the IOB format.
    """
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text().strip()

    # Tokenize by spaces, preserving punctuation
    words = re.findall(r'\S+|\s+', text) 

    iob_lines = []
    for word in words:
        if word == '.':
            iob_lines.append(f'{word}\tO\n')
        elif word.strip():  # Only process non-empty strings
            # Split words that contain '.' into separate words
            parts = word.split('.')
            for part in parts:
                if part:  
                    iob_lines.append(f'{part}\tO\n') 
        else:
            # If it's just whitespace, don't add it to iob_lines
            pass 

    iob_lines.append('\n')  # Add sentence boundary
    return iob_lines

def process_html_files(html_folder, output_file):
    """
    Processes all HTML files in a folder and converts them to IOB format,
    dumping the results into a single file.

    Args:
        html_folder: Path to the folder containing HTML files.
        output_file: Path to the output IOB file.
    """
    iob_data = []
    for filename in os.listdir(html_folder):
        if filename.endswith(".html"):
            html_file = os.path.join(html_folder, filename)
            iob_data.extend(convert_html_to_iob(html_file))

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(iob_data)


html_folder = r"C:\Users\archishman vb\OneDrive\Desktop\FSIL-GA-Tech\html_files"
output_file = r"C:\Users\archishman vb\OneDrive\Desktop\FSIL-GA-Tech\processed.iob"

process_html_files(html_folder, output_file)