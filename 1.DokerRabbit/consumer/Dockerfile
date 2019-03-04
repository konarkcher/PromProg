FROM python:3.7-alpine
ADD . /consumer
WORKDIR /consumer
RUN pip install -r requirements.txt
CMD ["python", "-u", "consumer.py"]
