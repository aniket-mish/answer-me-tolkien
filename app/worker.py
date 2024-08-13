from src.query_db import query_app

def query_handler(event):
    query = event
    invoke_model(query)

def invoke_model(query):
    res = query_app(query)
    print(f"Response from model: {res}")
    return res