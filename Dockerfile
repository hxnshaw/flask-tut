FROM python:3.12-slim-buster

WORKDIR /flask-app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

WORKDIR /flask-app/flask_tutorial

RUN flask db init
RUN flask db migrate
RUN flask db ugrade

WORKDIR /flask-app

CMD ["python3","run.py"]
