from pdf2image import convert_from_path
import pytesseract
import os

temp_folder = os.path.join(os.path.dirname("__file__"), "temp")

def extract_text(pdf_filename):
    path = os.path.join(temp_folder, pdf_filename)

    
