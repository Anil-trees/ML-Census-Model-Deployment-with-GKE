FROM python:3.7-slim-buster

# Change the COPY command to copy the entire directory to /app
COPY ./ml-census/requirements.txt /app/requirements.txt
COPY ./ml-census/model_deployment.py /app/model_deployment.py
COPY ./ml-census/model_deployment.yaml /app/model_deployment.yaml
COPY . /app

# Switch to the /app directory to execute subsequent commands
WORKDIR /app

# Install dependencies from requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

