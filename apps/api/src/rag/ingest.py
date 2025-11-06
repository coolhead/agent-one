import argparse, glob, os
from src.rag.store import DB
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from .store import DB

def main(path):
    files = glob.glob(os.path.join(path, "**/*.*"), recursive=True)
    docs=[]
    for f in files:
        try:
            docs += TextLoader(f, autodetect_encoding=True).load()
        except: pass
    chunks = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=120).split_documents(docs)
    DB.add_documents(chunks); DB.persist()
    print(f"Ingested {len(chunks)} chunks")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--path", required=True)
    main(ap.parse_args().path)
