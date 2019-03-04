FROM python:3.7-alpine
ADD . /producer
WORKDIR /producer
RUN pip install -r requirements.txt
CMD ["python", "-u", "producer.py"]
