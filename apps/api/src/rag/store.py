from typing import Any
from langchain_chroma import Chroma

try:
    from langchain_community.vectorstores import Chroma
    from langchain_huggingface import HuggingFaceEmbeddings
    EMB = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    DB = Chroma(collection_name="agent_one", embedding_function=EMB, persist_directory=".chroma")
    retriever = DB.as_retriever(search_kwargs={"k": 8})
except Exception:
    class _NoRetriever:
        def get_relevant_documents(self, q: str) -> list[Any]:
            return []
    retriever = _NoRetriever()
