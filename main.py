import convert, extract
import os, time

def answer(file_path):
    filename = os.path.basename(file_path)
    extension = file_path.split(".")[-1]

    convert.convert_to(file_path)

    result_pages = extract.extract_text(".".join(filename.split(".")[:-1]) + ".pdf")

    for i, page in enumerate(result_pages):
        print(page)
        print()

if __name__ == "__main__":
    # answer(input("Enter a file path: "))
    answer("/home/robin/Downloads/test4.docx")