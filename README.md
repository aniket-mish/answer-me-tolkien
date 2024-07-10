# toy-rag

This is a simple RAG application built using langchain and chroma database.

1. Store the API key in the `.env` file.

2. Create a database

`python create_db.py`

4. Query the llm with context from the vector db

`python query_db.py "what happened to gandalf that turned him white?"`

I have used cohere's embedding and the chat models.

I have used lotr books as the source data.

![output](assets/output.png)
