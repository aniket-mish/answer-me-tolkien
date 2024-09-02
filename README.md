# answer-me-tolkien

This is a simple RAG-based application built using langchain and chroma database.

## How to use

1. Store the API key in the `.env` file.

2. Create a database

```bash
python -m rag_app_image.src.create_db
```

3. Or update the database

```bash
python -m rag_app_image.src.update_db
```

4. Query the llm with context from the vector db

```bash
python -m rag_app_image.src.query_db "what happened to gandalf that turned him white?"
```

I have used cohere's embedding and the chat models.

> [!NOTE]
> If you want to run models locally, use Ollama

## Data I've used

I have used lotr material as the source data.

## Output I'm getting


![output](app/assets/output.png)


---

## Create a backend using AWS Lambda

Let's now extend the project to include a serverless backend and a fastHTML frontend.

![architecture](app/assets/architecture.png)

### Dockerize the app

I'm using an container image to deploy the code on AWS Lambda.

Remember to use Lambda supported base image.

> [!WARNING]
> Need to install pysqlite for chroma db to work correctly

See the [dockerfile](app/Dockerfile) for more details.

### Provision resources using AWS CDK

> [!NOTE]
> API Gateway has a time-limit of 30 seconds
> Lambda functions have a 15 minute time-limit

Install CDK and setup a project. You can specify the programming language as well. I prefer python but a lot of people like to typescript to write CDK templates.

```bash
cdk init app --language python
```

AWS recommends to run [bootstrap](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) before deploying the stack. It prepares the environment.

```bash
cdk bootstrap
```

To deploy the stack on AWS

```bash
cdk deploy
```

> [!WARNING]
> Delete the stack created once you're done experimenting

```bash
cdk destroy
```

