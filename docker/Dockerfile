FROM python:3.11.1

SHELL ["/bin/bash", "-c"]

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get upgrade -y \
  && apt-get install -y git zip unzip wget curl vim

RUN mkdir /code
WORKDIR /code
COPY ./config/requirements.txt /code/
# pipenv未使用
# RUN pip install --upgrade pip && pip install -r ./requirements.txt
RUN pip install --upgrade pip && pip install pipenv
# pipenv使用
RUN pipenv install -r ./requirements.txt
RUN pipenv install

COPY . /code/