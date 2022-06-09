#!/usr/bin/python3

import pdfplumber
from docx import Document
from gtts import gTTS
from pathlib import Path

file = input("Input file path:")
file_lang = input("Input file language(ru/en):")

def read_pdf_file():
    with pdfplumber.PDF(open(file=file, mode='rb')) as pdf:
        pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        audio_file = gTTS(text=text, lang=file_lang)
        file_name = Path(file).stem
        audio_file.save(f'{file_name}.mp3')

        print(f'File {file_name}.mp3 has been created')

def read_docx_file():
        document = Document(file)
        text = []
        for paragraph in document.paragraphs:
            text.append(paragraph.text)
        text = ''.join(text)
        text = text.replace('\n', '')

        audio_file = gTTS(text=text, lang=file_lang)
        file_name = Path(file).stem
        audio_file.save(f'{file_name}.mp3')

        print(f'File {file_name}.mp3 has been created')

def read_txt_file():
    with open(file, "r") as txt:
        text = []

        page = txt.read()
        text = page.replace('\n', '')

        audio_file = gTTS(text=text, lang=file_lang)
        file_name = Path(file).stem
        audio_file.save(f'{file_name}.mp3')

        print(f'File {file_name}.mp3 has been created')

def to_mp3(file_path=file, lang='file_lang'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print('[+] FILE FOUND')
        print('[+] PROCESSING...')
        read_pdf_file()
        print('[+] DONE!')
    elif Path(file_path).is_file() and Path(file_path).suffix == '.txt':
        print('[+] FILE FOUND')
        print('[+] PROCESSING...')
        read_txt_file()
        print('[+] DONE!')
    elif Path(file_path).is_file() and Path(file_path).suffix == '.doc' or '.docx':
        print('[+] FILE FOUND')
        print('[+] PROCESSING...')
        read_docx_file()
        print('[+] DONE!')
    else:
        print('[-] FILE NOT FOUND :(')

def main():
    print(to_mp3(file_path=file, lang=file_lang))

if __name__ == '__main__':
    main()
