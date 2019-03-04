import time
import sys

import pika


def callback(ch, method, properties, body):
    print(body.decode('utf-8'))


param = pika.ConnectionParameters('query', 5672)

while True:
    try:
        connection = pika.BlockingConnection(param)
        print('Consumer connected!', file=sys.stderr, flush=True)

        channel = connection.channel()
        channel.queue_declare(queue='random')

        channel.basic_consume(callback, queue='random', no_ack=True)
        channel.start_consuming()

    except (pika.exceptions.ConnectionClosed, OSError):
        print('Error, retrying', file=sys.stderr, flush=True)
        time.sleep(1)

