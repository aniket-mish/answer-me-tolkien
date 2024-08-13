# https://hub.docker.com/r/amazon/aws-lambda-python 
FROM public.ecr.aws/lambda/python:3.10

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the necessary build tools
RUN yum update -y && yum install -y gcc

# Required to install chromadb https://docs.trychroma.com/troubleshooting
RUN pip install pysqlite3-binary

# Install the packages
RUN pip install -r requirements.txt --upgrade

# Local test
EXPOSE 8000

# Enviornment variable to check if we're running a container
ENV IS_CONTAINER_RUNTIME=True

# Copy all required files
COPY src/* ${LAMBDA_TASK_ROOT}/src
COPY chroma ${LAMBDA_TASK_ROOT}/chroma
COPY data ${LAMBDA_TASK_ROOT}/data
COPY api_handler.py ${LAMBDA_TASK_ROOT}