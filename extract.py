from pdf2image import convert_from_path
import pytesseract
import os

temp_folder = os.path.join(os.path.dirname("__file__"), "temp")

def extract_text(pdf_filename):
    result_text = []

    path = os.path.join(temp_folder, pdf_filename)

    for page_png in convert_from_path(path):
        text = pytesseract.image_to_string(page_png, lang='eng')
        print(text)

        result_text.append(text)

    return result_text

if __name__ == "__main__":
    pdf_filename = input("Enter filename: ")
    extract_text(pdf_filename)