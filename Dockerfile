FROM python:3.11-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./aerich /code/aerich
COPY ./data_rates.json /code/
COPY ./fill_db.py /code/
