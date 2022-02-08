FROM python:3.9

WORKDIR /app

COPY app ./
COPY requirements.txt ./requirements.txt

RUN apt-get update && apt-get -y upgrade && apt-get -y install python3-pip
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD [ "python", "app.py"]

