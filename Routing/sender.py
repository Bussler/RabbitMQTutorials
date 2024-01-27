# logging system that sends messages to the queue. The messages are sent to multiple consumers that will be subscribed to the queue.

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# fanout exchange broadcasts all the messages it receives to all the queues it knows.
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

message = " ".join(sys.argv[1:]) or "Hello World!"
severity = "urgent" if message.count("!") >= 1 else 'info'

# publish a message to the exchange, not to a queue.
# Specify a routing_key parameter to indicate which queue the message should go to.
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)

print(f" [x] Sent {message}")

connection.close()