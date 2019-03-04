import random
import time
import sys

import pika

param = pika.ConnectionParameters('query', 5672)

while True:
    try:
        connection = pika.BlockingConnection(param)
        print('Producer connected!', file=sys.stderr, flush=True)

        channel = connection.channel()
        channel.queue_declare(queue='random')

        while True:
            interval = random.randint(0, 5)
            num = random.randint(0, 100)

            channel.basic_publish(exchange='',
                                  routing_key='random', body=str(num))
            time.sleep(interval)

    except (pika.exceptions.ConnectionClosed, OSError):
        print('Error, retrying', file=sys.stderr, flush=True)
        time.sleep(1)
