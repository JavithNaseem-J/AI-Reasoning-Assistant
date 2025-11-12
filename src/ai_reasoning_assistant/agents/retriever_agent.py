from langchain.vectorstores import Chroma

class RetrieverAgent:
    def __init__(self, persist_dir="data/embeddings"):
        self.vectordb = Chroma(persist_directory=persist_dir)
    
    def retrieve(self, query, k=3):
        results = self.vectordb.similarity_search(query, k=k)
        context = "\n".join([r.page_content for r in results])
        return context
