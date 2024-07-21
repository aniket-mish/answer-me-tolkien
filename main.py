from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from query_db import query_app

app = FastAPI()

class QueryRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/query")
async def post_query(query: QueryRequest):
    return query_app(query.text)