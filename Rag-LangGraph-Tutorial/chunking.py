## Fixed Sized Chunking 
### How it works: Cutting at exact Intervals (eg: every 500 chars)
# Chunk1: The quick brown fox jum \n
# Chunk2: ps over the la \n
# Chunk3: zy dog \n
#### These are too fragmented and useless in Rag
#_____________________________________________________________

## Recursive Chunking
# 80% of production RAG uses this Good balance : quality + speed

## Semantic Chunking (Best Quality)
# Splits at MEANING boundaries not arbitary points.

## Late Chunking (Latest Trend)
# Combines multiple small chunks into large semantically rich chunks before LLM call.

from langchain_huggingface import HuggingFaceEmbeddings
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

## Chat model

client = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.7)
client_embed = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

response = client.invoke(
    [
        ("system", "You are a helpful assistant."),
        ("human", "What is the capital of India? (only one word answer)")
    ],
    model="llama-3.3-70b-versatile"
)

print(response.content)

## Embedding model

response = client_embed.embed_query(
    "Hey hello my friend, how are you?"
)

print(len(response))