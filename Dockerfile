FROM python:3.7 as base

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./bin /app/bin/

RUN chmod u+x bin/*
RUN pip install --upgrade pip && pip install pipenv

COPY Pipfile* ./

RUN pipenv install --deploy
COPY . .

CMD pipenv run app
