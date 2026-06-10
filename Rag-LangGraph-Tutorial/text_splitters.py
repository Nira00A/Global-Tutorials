from langchain_text_splitters import RecursiveCharacterTextSplitter,  TextSplitter, MarkdownHeaderTextSplitter, CharacterTextSplitter
from langchain_core.documents import Document
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

SAMPLE_TEXT = """
# The Power of Vector Databases for AI

## What is a Vector Database?
At its core, a vector database is a specialized database designed to store, manage, and search high-dimensional vectors efficiently.

In the age of Artificial Intelligence, almost every interaction—from image recognition to natural language understanding—is converted into a vector (a list of numbers). A vector database makes it possible to search through these numerical representations based on their meaning and context.

## Why "Similarity" Matters
Unlike traditional databases that look for exact keyword matches, vector databases excel at understanding semantic similarity.

Imagine you search for "big cats." A traditional database might miss "tigers" or "lions" if the words aren't present. A vector database, however, understands that the vector representation of "big cats" is close to the vectors of "tigers" and "lions," and thus returns relevant results.

## Key Benefits
1. **Semantic Search**: Find information based on meaning, not just keywords.
2. **Scalability**: Handle millions or billions of vectors with ease.
3. **Hybrid Search**: Combine vector search with traditional metadata filtering.

## Popular Providers
- **Chroma**: Open-source and easy to use.
- **Pinecone**: Cloud-native and highly scalable.
- **Weaviate**: GraphQL API with advanced features.

Ready to supercharge your AI application? Start by implementing a vector database today!
"""

SAMPLE_CODE = """
# Binary Search

def binary_search(arr, target):
    Performs binary search on a sorted list.
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
sorted_list = [1, 3, 5, 7, 9, 11]
target = 7
index = binary_search(sorted_list, target)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")

# Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    Performs inorder traversal of a binary tree.
    result = []
    if root:
        result.extend(inorder_traversal(root.left))
        result.append(root.val)
        result.extend(inorder_traversal(root.right))
    return result

# Example usage
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(inorder_traversal(root))
"""

def recursive_splitter():
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20,
        separators=["\n\n", "\n", ".", " "],
    )

    chunks = splitter.split_text(SAMPLE_TEXT)
    
    print(f"Original length: {len(SAMPLE_TEXT)}")
    print(f"Number of chunks: {len(chunks)}")
    print(f"Chunk sizes: {[len(c) for c in chunks]}")
    print(f"Chunk preview: {chunks[0]}")

def overlap_importance():
    text= "The quick fox is dancing and laughing around" * 10

    withOverlap = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )
    withoutOverlap = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=0
    )

    chunksWithOverlap = withOverlap.split_text(text)
    chunksWithoutOverlap = withoutOverlap.split_text(text)
    
    print(f"Chunks with overlap: {len(chunksWithOverlap)}")
    print(f"Chunks without overlap: {len(chunksWithoutOverlap)}")
    print(f"First chunk with overlap: {chunksWithOverlap[0]}")
    print(f"First chunk without overlap: {chunksWithoutOverlap[0]}")

if __name__ == "__main__":
    overlap_importance()
