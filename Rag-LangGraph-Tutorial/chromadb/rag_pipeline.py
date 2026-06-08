from langchain_groq import ChatGroq
from langchain_core.documents import Document
import os
from typing import TypedDict
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
import dotenv

dotenv.load_dotenv()

KNOWLEDGE_BASE = """# LangChain Framework
LangChain is a framework for developing applications powered by language models. It was created by Harrison Chase in October 2022.
## Core Components
1. **Models**: LangChain supports various LLM providers including OpenAI, Anthropic, and local models.
2. **Prompts**: Templates for structuring inputs to language models.
3. **Chains**: Sequences of calls to models and other components.
4. **Agents**: Systems that use LLMs to determine which actions to take.
5. **Memory**: Components for persisting state between chain/agent calls.
## LangGraph
LangGraph is a library for building stateful, multi-actor applications. Key features:
- State management
- Cycles and loops
- Human-in-the-loop
- Persistence
## Pricing
LangChain itself is open source and free. LangSmith (the observability platform) has a free tier and paid plans starting at $39/month.
## Getting Started
Install with: pip install langchain langchain-openai
Create your first chain in under 10 lines of code.
"""

class GraphState(TypedDict):
    """Represents the state of our graph."""
    question: str
    context: str
    answer: str

def create_kb():
    """Init the vector store to store the data"""
    documents = Document(
        page_content=KNOWLEDGE_BASE,
        metadata={"source": "langchain_framework", "topic": "programming", "type": "text"}
    )
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    chunks = text_splitter.split_documents([documents])

    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        client=chromadb.Client(),
        persist_directory="./kb_data"
    )
    print("Vector store created and persisted to ./kb_data")

    return vector_store

def retrive_node(state: GraphState):
    """Fetches relevant documents based on the question."""
    vector_store= create_kb()
    retriver = vector_store.as_retriever(search_kwargs={"k": 2})

    docs = retriver.invoke(state["question"])
    context = "\n".join([doc.page_content for doc in docs])

    return {"context": context}

def responder_node(state: GraphState):
    """Responds to the question using the retrieved context."""
    model = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.2
    )
    
    prompt = ChatPromptTemplate.from_template(
        """Answer the question based on the context provided.
        
        Context: {context}
        Question: {question}
        """
    )

    chain = prompt | model
    response = chain.invoke(state)
    return {"answer": response.content}

def execute_rag():
    workflow = StateGraph(GraphState)
    workflow.add_node("retrieve_node", retrive_node)
    workflow.add_node("responder_node", responder_node)

    workflow.add_edge(START, "retrieve_node")
    workflow.add_edge("retrieve_node", "responder_node")
    workflow.add_edge("responder_node", END)

    app = workflow.compile()
    response = app.invoke({
        "question": "What is LangSmith?"
    })

    print(response)

if __name__ == "__main__":
    execute_rag()
