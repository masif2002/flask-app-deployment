FROM python:3.10.7-slim-buster

RUN mkdir -p /home/app/web2
WORKDIR /home/app/web2

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .