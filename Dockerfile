FROM python:3.11-slim

WORKDIR /app

RUN pip install pipenv

COPY app/models models
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --ignore-pipfile --system

COPY depression_predictor .

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 app:app