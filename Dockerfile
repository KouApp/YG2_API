# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /main

COPY requirements.txt requirements.txt
RUN apt-get update \
  && apt-get -y install gcc \
  && apt-get -y install g++ \
  && apt-get -y install unixodbc unixodbc-dev \
  && apt-get clean`
  
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
