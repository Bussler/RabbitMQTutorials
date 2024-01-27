# logging system that sends messages to the queue. The messages are sent to multiple consumers that will be subscribed to the queue.

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# fanout exchange broadcasts all the messages it receives to all the queues it knows.
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = " ".join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

print(f" [x] Sent {message}")

connection.close()