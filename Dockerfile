# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /main

COPY requirements.txt requirements.txt

RUN apt-get update
RUN apt-get install -y apt-transport-https
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
  
RUN apt-get update && apt-get install -y gcc unixodbc-dev

  
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
