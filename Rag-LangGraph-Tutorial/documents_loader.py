import os
import tempfile
from pathlib import Path
from langchain_community.document_loaders import ( TextLoader , PyPDFLoader)
from dotenv import load_dotenv

def load_text_file():
    # Create a temporary text file for demostration
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file.write(b"Hello, this is a sample text file.\nThis file is used to train the model")
        temp_file_path = temp_file.name

    try:
        loader = TextLoader(temp_file_path)
        documents = loader.load()

        for doc in documents:
            print(doc)
            print(doc.page_content)
            print(doc.metadata)
    finally:
        os.remove(temp_file_path)

def load_pdf_file():
    try:
        loader = PyPDFLoader(file_path="./datafiles/Infocera-JD.pdf")
        documents = loader.load()

        for doc in documents:
            print(doc)
            print(doc.page_content)
            print(doc.metadata)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    load_pdf_file()