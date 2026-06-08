from dotenv import load_dotenv
from importlib.metadata import version

load_dotenv()

core_version = version("langchain-core")
lg_version = version("langgraph")

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

def main():
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
    print(llm.invoke("Hello, how are you in one word?"))

    print(f"Core Version : {core_version}")
    print(f"LangGraph Version : {lg_version}")

if __name__ == "__main__":
    main()