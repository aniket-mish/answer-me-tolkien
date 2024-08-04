import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_cohere import CohereEmbeddings
from src.preprocess import load_docs, split_docs

load_dotenv()

DB_PATH = "chroma"
DATA_PATH = "new_data"

# saves as a sqlite3 file
def update_the_database(chunks):

    # create the open-source embedding function
    embedding_function = CohereEmbeddings(model="embed-english-light-v3.0")

    # load it into Chroma
    db = Chroma(embedding_function=embedding_function, persist_directory=DB_PATH)

    # check for existing documents
    existing_items = db.get(include=[])
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in the db: {len(existing_ids)}")

    # get new documents
    new_chunks = []
    for chunk in chunks:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)
    
    # get new document ids
    new_chunk_ids = []
    for chunk in new_chunks:
        new_chunk_ids.append(chunk.metadata["id"])

    # update the db with new documents
    print(f"Number of new documents to add in the db: {len(new_chunks)}")
    db.add_documents(new_chunks, ids=new_chunk_ids)

    print(f"{len(chunks)} chunks are now stored in chroma")

def generate_db():
    documents = load_docs(DATA_PATH)
    chunks = split_docs(documents)
    update_the_database(chunks)

def main():
    generate_db()


if __name__ == "__main__":
    main()
