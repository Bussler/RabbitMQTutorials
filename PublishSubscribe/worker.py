#!/usr/bin/env python
import pika, sys, os
import time

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

    # declare a queue with a random name, exclusive=True, so that queue is deleted when the consumer connection is closed.
    # name of queue can be read from result.method.queue
    result_queue = channel.queue_declare(queue='', exclusive=True)
    
    # bind the queue to the exchange: like a subscription to get all incoming messages
    channel.queue_bind(exchange='logs',
                   queue=result_queue.method.queue)

    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        time.sleep(body.count(b'.') )
        print(" [x] Done")
        # ch.basic_ack(delivery_tag = method.delivery_tag)

    channel.basic_consume(queue=result_queue.method.queue, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)