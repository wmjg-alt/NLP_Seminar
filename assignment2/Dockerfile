# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /assignment2

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 -m spacy download en_core_web_sm

COPY . .

CMD [ "python3", "app.py"]