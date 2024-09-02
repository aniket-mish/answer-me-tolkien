FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt ${LAMBDA_TASK_ROOT}

# https://docs.trychroma.com/troubleshooting
RUN pip install pysqlite3-binary

RUN pip install -r requirements.txt --upgrade

EXPOSE 8080

ENV IS_CONTAINER_RUNTIME=False

COPY src/* ${LAMBDA_TASK_ROOT}/src
COPY chroma ${LAMBDA_TASK_ROOT}/chroma
COPY data ${LAMBDA_TASK_ROOT}/data
COPY api_handler.py ${LAMBDA_TASK_ROOT}