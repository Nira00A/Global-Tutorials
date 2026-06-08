from langchain_core.documents import Document
from langchain_text_splitters import TextSplitter , RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
import chromadb
import numpy as np
from langchain_huggingface import HuggingFaceEmbeddings

documents = [
    Document(page_content="Programming is a creative process that involves thinking", metadata={"source": "programming", "type": "text"}),
    Document(page_content="Data science is an interdisciplinary field that uses scientific methods", metadata={"source": "data science", "type": "text"}),
    Document(page_content="Machine learning is a subset of artificial intelligence", metadata={"source": "machine learning", "type": "text"}),
    Document(page_content="Deep learning is a subset of machine learning", metadata={"source": "deep learning", "type": "text"}),
    Document(page_content="Neural networks are the foundation of deep learning", metadata={"source": "neural networks", "type": "text"}),
    Document(page_content="Artificial intelligence is a broad field of computer science", metadata={"source": "artificial intelligence", "type": "text"}),
]

def similarity_search():
    embedding = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embedding,
        client=chromadb.Client(),
        persist_directory="./kb_data"
    )

    docs = [doc.page_content for doc in documents]
    docs_vector = embedding.embed_documents(docs)

    query = "what is programming?"
    query_vector = embedding.embed_query(query)
    
    def cosine_similarity(vec1,vec2):
        return np.dot(vec1,vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2))

    similarity = [cosine_similarity(query_vector,document_vector) for document_vector in docs_vector]

    similarity_dict = dict(zip(docs,similarity))
    sorted_similarity = sorted(similarity_dict.items(),key=lambda x:x[1],reverse=True)
    
    print(f"Query: {query}\n\n")

    for doc,score in sorted_similarity:
        print(f"Score: {score:.4f}, Text: {doc}")

if __name__ == "__main__":
    similarity_search()