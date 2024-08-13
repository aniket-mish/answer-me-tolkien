from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_docs(directory):
    """
    load data from a source
    """

    loader = DirectoryLoader(directory, glob="*.txt")
    docs = loader.load()
    return docs

def split_docs(documents):
    """
    split documents into smaller chunks
    """
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 50,
        length_function = len,
        add_start_index = True
    )
    chunks = text_splitter.split_documents(documents)

    for chunk in chunks:
        chunk_id = chunk.metadata["start_index"]
        chunk.metadata["id"] = f"{chunk.metadata['source']}_{chunk_id}"

    return chunks
