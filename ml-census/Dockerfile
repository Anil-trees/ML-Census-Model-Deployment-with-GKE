FROM python:3.7-slim-buster

# Change the COPY command to copy the entire directory to /app
COPY . /app

# Switch to the /app directory to execute subsequent commands
WORKDIR /app

# Install dependencies from requirements.txt
COPY ./ml-census/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

