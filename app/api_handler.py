from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum

from src.query_db import query_app


app = FastAPI()
handler = Mangum(app)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/query")
def post_query(query):
    return query_app(query)