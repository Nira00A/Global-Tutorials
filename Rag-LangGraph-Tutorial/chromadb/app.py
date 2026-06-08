from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
import tempfile
import chromadb
from langchain_chroma import Chroma
chroma_client = chromadb.Client()

documents = [
        {"text": "The quick brown fox jumps over the lazy dog.", "id": "doc1"},
        {"text": "My name is Arin.", "id": "doc2"},
        {"text": "I am a software engineer.", "id": "doc3"},
        {"text": "I am a data scientist.", "id": "doc4"},
        {"text": "I am from uganda im a software engineer from uganda", "id": "doc5"},
        {"text": "Name is modon", "id": "doc6"},
        {"text": "Longing cha mne mo", "id": "doc7"}
    ]

documents_w_meta = [
    Document(
        page_content="The quick brown fox jumps over the lazy dog.",
        metadata={"topic": "animal"}
    ),
    Document(
        page_content="My name is Arin.",
        metadata={"topic": "name"}
    ),
    Document(
        page_content="I am a software engineer.",
        metadata={"topic": "job"}
    ),
    Document(
        page_content="I am a data scientist.",
        metadata={"topic": "job"}
    ),
    Document(
        page_content="I am from uganda im a software engineer from uganda",
        metadata={"topic": "job"}
    ),
    Document(
        page_content="Name is modon",
        metadata={"topic": "name"}
    ),
    Document(
        page_content="Longing cha mne mo",
        metadata={"topic": "longing"}
    )
]

def chroma_basics():
    collection_name = "text_collection"

    collection = chroma_client.get_or_create_collection(collection_name)

    for docs in documents:
        collection.add(
            ids=docs["id"],
            documents=docs["text"]
        )

    query = "What is my name?"

    results = collection.query(
        query_texts=query,
        n_results=2
    )

    print(results)

def similarity_search():
    with tempfile.TemporaryDirectory() as tmpdir:
        text = [doc["text"] for doc in documents]

        vector_store = Chroma.from_texts(
            texts=text,
            embedding=HuggingFaceEmbeddings(
                model_name="BAAI/bge-small-en-v1.5"
            ),
            client=chroma_client,
            collection_name="text_collection",
            persist_directory=tmpdir
        )

        query = "What is my name?"

        results = vector_store.similarity_search_with_score(
            query=query,
            k=3
        )

        print(f"Top 3 results with scores for query '{query}':\n")
        for i, (doc, score) in enumerate(results, start=1):
            print(f"{i}. Score: {score:.4f}, Text: {doc.page_content}")

def metadata_filtering():
    with tempfile.TemporaryDirectory() as tmpdir:
        text = [doc["text"] for doc in documents]

        vector_store = Chroma.from_documents(
            documents=documents_w_meta,
            embedding=HuggingFaceEmbeddings(
                model_name="BAAI/bge-small-en-v1.5"
            ),
            client=chroma_client,
            collection_name="text_collection",
            persist_directory=tmpdir
        )

        query = "What is my name?"

        results = vector_store.similarity_search_with_score(
            query=query,
            k=3
        )

        print(f"Top 3 results with scores for query '{query}':\n")
        for i, (doc, score) in enumerate(results, start=1):
            print(f"{i}. Score: {score:.4f}, Text: {doc.page_content}")

        ## with meta data filtering
        filter_criteria = {"topic": "name"}
        filtered_results = vector_store.similarity_search(
            query, 
            k= 3,
            filter=filter_criteria
        )    

        print(f"\nResults after filtering:")
        for i, doc in enumerate(filtered_results, start=1):
            print(f"{i}. {doc.page_content}")

if __name__ == "__main__":
    metadata_filtering()

