import os
from langchain.text_splitter import RecursiveCharacterTextSpliter
import LOADFILES
import CHUNKING
path = "C:/Users/Prateek/OneDrive/Desktop/RAGDocs"
textValueOfWord = ""
textValueOfPDF = ""
for file in os.listdir(path):
    filepath = os.path.join(path,file)
    if file.endswith(".docx"):
        textValueOfWord = LOADFILES.load_word(filepath)

    elif file.endswith(".pdf"):
        textValueOfPDF = LOADFILES.load_pdf(filepath)

    elif file.endswith(".xlsx"):
        print("Excel")
       #LOADFILES.load_excel(filepath)
    else:
        print("Not an file")
print ("Text Values Of Word : ", textValueOfWord)
print("Text Values Of PDF: ", textValueOfPDF)
CHUNKING.FileChunking(textValueOfWord)



