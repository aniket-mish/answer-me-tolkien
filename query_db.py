import os
import argparse
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_cohere import ChatCohere
from langchain_cohere import CohereEmbeddings
from langchain_core.prompts import PromptTemplate

load_dotenv()

PROMPT_TEMPLATE = f"""
Context information is below.
---------------------
{context}
---------------------
Given the context information and not prior knowledge, answer the query.
Query: {query}
Answer:
"""

def main():
    """
    query the db
    """

    # create a CLI
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str)
    args = parser.parse_args()
    query = args.query

    # create the open-source embedding function
    embedding_function = CohereEmbeddings(model="embed-english-light-v3.0")

    # prepare the db
    db = Chroma(persist_directory="chroma", embedding_function=embedding_function)

    # search the db
    results = db.similarity_search_with_score(query, k=3)

    if len(results) == 0 or results[0][1] < 0.10:
        print("No matching documents found.")

    context = "\n\n----\n\n".join([doc.page_content for doc, score in results])
    
    # add context and query to the prompt
    prompt_template = PromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context, query=query)
    print(f"Prompt: \n {prompt}")

    # free 100 api calls per minute
    cohere_chat_model = ChatCohere()
    response = cohere_chat_model.invoke(prompt)
    print(f"Response: \n {response.content}")

if __name__ == "__main__":
    main()