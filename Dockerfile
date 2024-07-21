# https://hub.docker.com/r/amazon/aws-lambda-python 
FROM public.ecr.aws/lambda/python:3.10

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the packages
RUN pip install -r requirements.txt --upgrade

# Local test
EXPOSE 8000

# Copy all required files
COPY src/* ${LAMBDA_TASK_ROOT}
COPY chroma ${LAMBDA_TASK_ROOT}/chroma
COPY data ${LAMBDA_TASK_ROOT}/data