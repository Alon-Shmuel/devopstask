# syntax=docker/docker:1
FROM ubuntu
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt update && apt install -y python3 python3-pip
RUN pip3 install -r requirements.txt
COPY . .
CMD python3 main.py

