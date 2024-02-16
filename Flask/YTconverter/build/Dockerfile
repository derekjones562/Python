# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /srv

RUN apt-get update && apt-get install -y git

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /srv
# ENV FLASK_APP=app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
# CMD ["python", "app.py"]