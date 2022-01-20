FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
RUN mkdir Django_project
WORKDIR /Django_project
COPY requirements.txt .
RUN pip install -r requirements.txt
