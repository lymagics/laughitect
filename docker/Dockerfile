FROM python:slim

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY blogger blogger
COPY waitlist waitlist
WORKDIR /blogger