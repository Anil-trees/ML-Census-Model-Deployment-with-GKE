FROM python:3.7-slim-buster

# Create the /app directory
WORKDIR /app

# Copy the entire directory to /app
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --upgrade pip && pip install -r /app/ml-census/requirements.txt --no-cache-dir


