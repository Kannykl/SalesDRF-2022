FROM python:3.10-slim
WORKDIR /sales

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install netcat -y
RUN pip install --upgrade pip

COPY requirements.txt /sales/requirements.txt
RUN pip install -r requirements.txt

COPY . /sales

ENTRYPOINT ["/sales/entrypoint.sh"]
