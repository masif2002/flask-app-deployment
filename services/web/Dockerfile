FROM python:3.10.7-slim-buster

# sets working directory in container
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

# For services to contact between them (in entrypoint.sh)
RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "./entrypoint.sh" ]