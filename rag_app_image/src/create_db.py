import os
import sys
import shutil
from dotenv import load_dotenv

IS_CONTAINER_RUNTIME = bool(os.environ.get("IS_CONTAINER_RUNTIME", False))

if IS_CONTAINER_RUNTIME:
    __import__("pysqlite3")
    sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

from langchain_chroma import Chroma
from langchain_cohere import CohereEmbeddings
from src.preprocess import load_docs, split_docs

load_dotenv()

DB_PATH = "chroma"
DATA_PATH = "data"

# saves as a sqlite3 file
def save_to_chroma_db():
    """
    convert chunks to embeddings and store them in the chroma db
    """

    documents = load_docs(DATA_PATH)
    chunks = split_docs(documents)

    # clear out the db
    if os.path.exists(DB_PATH):
        shutil.rmtree(DB_PATH)

    # create the embedding function
    embedding_function = CohereEmbeddings(model="embed-english-light-v3.0")

    # load it into chroma
    db = Chroma.from_documents(chunks, embedding_function, persist_directory=DB_PATH)
    print(f"{len(chunks)} chunks are now stored in chroma at {DB_PATH}.")

    return db


if __name__ == "__main__":
    db = save_to_chroma_db()