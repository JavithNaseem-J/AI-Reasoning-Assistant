import os
from langchain.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma

def build_vector_store(data_path="data/docs", persist_dir="data/embeddings"):
    loaders = [
        DirectoryLoader(data_path, glob="*.txt", loader_cls=TextLoader),
        DirectoryLoader(data_path, glob="*.pdf", loader_cls=PyPDFLoader)
    ]
    docs = []
    for loader in loaders:
        docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
    chunks = splitter.split_documents(docs)

    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    vectordb = Chroma.from_documents(chunks, embeddings, persist_directory=persist_dir)
    vectordb.persist()
    print(f"✅ Vector DB built with {len(chunks)} chunks.")
    return vectordb

if __name__ == "__main__":
    build_vector_store()
