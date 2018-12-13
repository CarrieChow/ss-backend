FROM python:2.7

MAINTAINER engineering@sourcesage.co

WORKDIR /app

ADD requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
