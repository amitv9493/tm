FROM python:3.8
WORKDIR /app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip 

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc && \
    apt-get clean
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt
COPY . .



