#!/usr/bin/env python

__author__ = 'theofilis'

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

for i in range(1000000):
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')

connection.close()