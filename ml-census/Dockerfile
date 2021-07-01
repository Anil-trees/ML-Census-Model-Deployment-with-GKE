FROM python:3.7-slim-buster
COPY . /app
RUN pip install --upgrade pip\
    pip install -r /app/requirements.txt --no-cache-dir
WORKDIR /app
