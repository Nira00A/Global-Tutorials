from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.retrievers import BM25Retriever
from langchain_core.retrievers import EnsembleRetriever
from langchain_core.documents import Document

from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

docs = [
    Document(
        page_content="Product SKU-77889X is our flagship router. It supports Wi-Fi 6E and has a 2Gbps",
        metadata={
            "product_id": "77889X",
            "type": "router",
        }
    ),
    Document(
        page_content="Product SKU-24501Y is a compact Wi-Fi 6 router. Ideal for small homes or apartments.",
        metadata={
            "product_id": "24501Y",
            "type": "router",
        }
    ),
    Document(
        page_content="Product SKU-11223Q is a gaming router with RGB lighting and liquid cooling.",
        metadata={
            "product_id": "11223Q",
            "type": "router",
        }
    ),
    Document(
        page_content="Product SKU-33445P is a Wi-Fi 6 mesh system extender. Use it to expand coverage.",
        metadata={
            "product_id": "33445P",
            "type": "router",
        }
    ),
    Document(
        page_content="Product SKU-88776R is a dual-band AC1200 router. Good for budget-conscious users.",
        metadata={
            "product_id": "88776R",
            "type": "router",
        }
    ),
    Document(
        page_content="Product SKU-55667S is a Wi-Fi 5 router, still reliable for basic internet needs.",
        metadata={
            "product_id": "55667S",
            "type": "router",
        }
    ),
    Document(
        page_content="Product SKU-44332V is a tri-band AX11000 gaming router with advanced QoS features.",
        metadata={
            "product_id": "44332V",
            "type": "router",
        }
    ),
    Document(
        page_content="Product SKU-99887T is a mesh Wi-Fi 6 system with three units for whole-home coverage.",
        metadata={
            "product_id": "99887T",
            "type": "router",
        }
    ),
    Document(
        page_content="Product SKU-22334U is a budget-friendly Wi-Fi 6 router suitable for small apartments.",
        metadata={
            "product_id": "22334U",
            "type": "router",
        }
    ),
    Document(
        page_content="Product SKU-66778W is a dual-band AC1750 router offering a balance of performance and price.",
        metadata={
            "product_id": "66778W",
            "type": "router",
        }
    ),
]

vector_store = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    collection_name="hybrid_search",
    persist_directory="./kb_data"
)

vector_retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)

bm25_retriever = BM25Retriever.from_documents(
    documents=docs,
    k=3
)

ensemble_retriever = EnsembleRetriever(
    retrievers=[vector_retriever, bm25_retriever],
    weights=[0.5, 0.5]
)

def test_query(query, name, retriever):
    """Helper function to test a retriever."""
    result = retriever.invoke(query)
    print(f'\n\n{name} - Query: {query}')

    for i,doc in enumerate(result[:3]):
        print(f"Retrieved Doc {i+1}: {doc.page_content}")

test_queries = [
    "Which product has 2Gbps speed?",
    "I need a router for a small apartment.",
    "What is SKU-11223Q?",
]

if __name__ == "__main__":
    test_query(test_queries,"Vector Store",vector_retriever)
    test_query(test_queries,"BM25",bm25_retriever)
    test_query(test_queries,"Ensemble Retriever",ensemble_retriever)