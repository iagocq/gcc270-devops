FROM python:3.7-alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV FLASK_APP=todolist

EXPOSE 5000

CMD python -m flask run -h 0.0.0.0 -p 5000
