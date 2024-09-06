FROM python:3.11.1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./config/requirements.txt /code/
RUN pip install --upgrade pip && pip install -r ./requirements.txt
COPY . /code/