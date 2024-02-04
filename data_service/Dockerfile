FROM python:3.10.6-alpine3.16
RUN apk add git build-base linux-headers libffi-dev
WORKDIR /data_service

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .


CMD ["python", "dev.py"]