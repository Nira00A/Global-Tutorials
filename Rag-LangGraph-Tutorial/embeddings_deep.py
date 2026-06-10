from langchain_huggingface import HuggingFaceEmbeddings
import numpy as np
from dotenv import load_dotenv

load_dotenv()


def basic_embeddings():
    text= "Hello, how are you?"
    embedding = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    single_embedding = embedding.embed_query(text)
    
    print(f"Generated Embedding first Five: {single_embedding[:5]}...")
    print(f"Embedding Dimension: {len(single_embedding)}")
    print(f"Normalize the vector: {np.linalg.norm(single_embedding)}")
    
def batch_embeddings():
    text ="""
    1. Apple Inc. is an American multinational technology company headquartered in Cupertino, California.
    2. The company was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976.
    3. Apple is known for its consumer electronics, software, and online services.
    4. Popular products include the iPhone, iPad, Mac, Apple Watch, and AirPods.
    5. The company's operating system for mobile devices is iOS, and for desktop computers is macOS.
    6. Apple has a global retail presence with over 500 stores worldwide.
    7. The App Store, launched in 2008, is a digital distribution platform for mobile apps.
    8. Tim Cook has served as the CEO of Apple since 2011.
    9. The company's services division includes Apple Music, iCloud, Apple TV+, and Apple Pay.
    10. Apple's research and development focuses on areas like artificial intelligence, augmented reality, and autonomous vehicles.
    """
    embedding = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    batched_embeddings = embedding.embed_documents(text)

    for i, embedding in enumerate(batched_embeddings):
        print(f"Document {i+1} Embedding: {embedding[:5]}...")
        print(f"Document {i+1} Embedding Dimension: {len(embedding)}")
        print(f"Document {i+1} Normalize the vector: {np.linalg.norm(embedding)}")

def similarity_search():
    text =[
    "1. Apple Inc. is an American multinational technology company headquartered in Cupertino, California.",
    "2. The company was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976.",
    "3. Apple is known for its consumer electronics, software, and online services.",
    "4. Popular products include the iPhone, iPad, Mac, Apple Watch, and AirPods.",
    "5. The company's operating system for mobile devices is iOS, and for desktop computers is macOS.",
    "6. Apple has a global retail presence with over 500 stores worldwide.",
    "7. The App Store, launched in 2008, is a digital distribution platform for mobile apps.",
    "8. Tim Cook has served as the CEO of Apple since 2011.",
    "9. The company's services division includes Apple Music, iCloud, Apple TV+, and Apple Pay.",
    "10. Apple's research and development focuses on areas like artificial intelligence, augmented reality, and autonomous vehicles.",
    ]

    embedding = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )
    
    query = "What is the mobile operating system for Apple devices?"

    docs_vector = embedding.embed_documents(text)
    query_vector = embedding.embed_query(query)

    def cosine_similarity(v1 , v2):
        """Calculate the cosine similarity between two vectors."""
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

    similarity_score = [cosine_similarity(query_vector , doc_vector) for doc_vector in docs_vector]

    ranked_docs = sorted(zip(text, similarity_score), key=lambda x: x[1], reverse=True)

    print(F"The query is: {query}\n")
    print("Ranked by similarity:\n")
    for doc, score in ranked_docs:
        print(f"Document: {score:.4f} {doc}")



# def similarity_search2():

#     # Documents

#     docs = [
#         "Python is a programming language",
#         "JavaScript is used for web development",
#         "Machine learning enables AI applications",
#         "Deep learning uses neural networks",
#         "Cats are popular pets",
#     ]

#     query = "What programming languages exist?"

#     embeddings_model = HuggingFaceEmbeddings(
#         model_name="BAAI/bge-small-en-v1.5"
#     )

#     # embed documents and query
#     doc_vector = embeddings_model.embed_documents(docs)
#     query_vector = embeddings_model.embed_query(query)

#     # compute cosine similarities
#     def cosine_similarity(vec1, vec2):
#         return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

#     similarities = [cosine_similarity(query_vector, doc_vec) for doc_vec in doc_vector]

#     # rank documents by similarity
#     ranked_docs = sorted(zip(docs, similarities), key=lambda x: x[1], reverse=True)

#     print(f"Query: {query}\n")
#     print("Ranked by similarity:")
#     for doc, score in ranked_docs:
#         print(f"  {score:.4f}: {doc}")

if __name__ == "__main__":
    similarity_search()
    