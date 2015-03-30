#!/usr/bin/env python

__author__ = 'theofilis'

from datetime import datetime

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='logstash')

time_at_current_location = datetime.now()

for i in range(1000):
    msg = "1,"
    msg += time_at_current_location.strftime("%Y-%m-%dT%H:%M:%SZ") + ","
    msg += "0,"
    msg += "31,"
    msg += "75,"
    msg += "38.0317237,23.6738527"

    channel.basic_publish(exchange='elasticsearch',
                          routing_key='logstash',
                          body=msg)

connection.close()