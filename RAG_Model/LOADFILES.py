import docx2txt as doctxt
from pypdf import PdfReader
import pandas as pd
class LOADFILES:
    def __init__(self,path):
        self.path = path
def load_word(filepath):
    print("inside word document")
    text: str = ""
    text += doctxt.process(filepath)
    #print("Text " + text)
    return text
def load_pdf(filepath):
    print("inside pdf document")
    reader = PdfReader(filepath)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
        #print("PDF Text" + text)
    return text
def load_excel(filename):
    df = pd.read_excel(filename)
    print("Excel data" + df.to_string())
    return df.to_string()