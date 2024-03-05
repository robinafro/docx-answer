import sys
import subprocess
import re
import os
from docx import Document

out_folder = os.path.join(os.path.dirname(__file__), "temp")

def convert_to(source, timeout=None):
    temp_filename = os.path.join(os.path.join(os.path.dirname(__file__), "temp"), os.path.basename(source))
    newdoc = Document(source)

    for paragraph in newdoc.paragraphs:
        for run in paragraph.runs:
            run.text = re.sub(r"_+", "[ Doplň zde ]", run.text)

    newdoc.save(temp_filename)

    args = [libreoffice_exec(), '--headless', '--convert-to', 'pdf', '--outdir', out_folder, temp_filename]

    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    filename = re.search('-> (.*?) using filter', process.stdout.decode())

    if filename is None:
        raise LibreOfficeError(process.stdout.decode())
    else:
        return filename.group(1)

def libreoffice_exec():
    # TODO: Provide support for more platforms
    if sys.platform == 'darwin':
        return '/Applications/LibreOffice.app/Contents/MacOS/soffice'
    return 'libreoffice'

class LibreOfficeError(Exception):
    def __init__(self, output):
        self.output = output

if __name__ == "__main__":
    convert_to(input("Input a file path: "))
