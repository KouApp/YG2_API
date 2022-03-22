# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /main

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y gcc unixodbc-dev
RUN sudo apt install python3-pip python3-dev unixodbc-dev
RUN pip3 install --user pyodbc
  
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
