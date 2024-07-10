import os
import shutil
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_cohere import CohereEmbeddings
from preprocess import load_docs, split_docs

load_dotenv()

DB_PATH = "chroma"
DATA_PATH = "data"

# saves as a sqlite3 file
def save_to_database(chunks):
    """
    convert chunks to embeddings and store them in the chroma db
    """

    # clear out the db
    if os.path.exists(DB_PATH):
        shutil.rmtree(DB_PATH)

    # create the embedding function
    embedding_function = CohereEmbeddings(model="embed-english-light-v3.0")
    print("save to chroma")

    # load it into chroma
    db = Chroma.from_documents(chunks, embedding_function, persist_directory=DB_PATH)

    print(f"{len(chunks)} chunks are now stored in chroma at {DB_PATH}.")

def generate_db():
    documents = load_docs(DATA_PATH)
    chunks = split_docs(documents)
    save_to_database(chunks)

def main():
    generate_db()


if __name__ == "__main__":
    main()