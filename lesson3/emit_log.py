# !/usr/bin/env python
__author__ = 'theofilis'

import sys

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='elasticsearch',
                         type='direct')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='elasticsearch',
                      routing_key='elasticsearch',
                      body=message)
print " [x] Sent %r" % (message,)
connection.close()