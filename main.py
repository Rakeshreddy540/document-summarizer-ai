import argparse
import os
import requests
from pdfminer.high_level import extract_text
from docx import Document
from bs4 import BeautifulSoup


def summarize_text(text):
    # Implement a simple summarization algorithm (for example using first n sentences or any other approach)
    return '\n'.join(text.split('. ')[:3])  # Modify summarization logic as necessary


def process_pdf(file_path):
    return extract_text(file_path)


def process_docx(file_path):
    doc = Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])


def process_txt(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def process_md(file_path):
    with open(file_path, 'r') as file:
        return file.read()  # Markdown processing can be enhanced if needed


def fetch_url_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def main():
    parser = argparse.ArgumentParser(description='Document Summarizer')
    parser.add_argument('input', help='Path to the document or URL to be summarized.')
    args = parser.parse_args()

    input_path = args.input
    text = ''

    if os.path.isfile(input_path):
        ext = os.path.splitext(input_path)[1].lower()
        if ext == '.pdf':
            text = process_pdf(input_path)
        elif ext == '.docx':
            text = process_docx(input_path)
        elif ext == '.txt':
            text = process_txt(input_path)
        elif ext == '.md':
            text = process_md(input_path)
        else:
            print('Unsupported file format!')
            return
    elif input_path.startswith('http'):
        text = fetch_url_content(input_path)
    else:
        print('Invalid input! Please provide a file path or URL.')
        return

    summary = summarize_text(text)
    print('Summary:')
    print(summary)


if __name__ == '__main__':
    main()