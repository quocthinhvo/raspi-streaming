FROM python:3.9.5-slim-buster

WORKDIR /app

COPY . .

RUN apt-get update 
RUN pip install -r requirements.txt

CMD ["python", "server.py"]