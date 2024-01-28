#!/usr/bin/env python
import pika, sys, os
import time

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    # declare an exchange of type direct: messages are routed to queues based on a message routing key
    channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

    # declare a queue with a random name, exclusive=True, so that queue is deleted when the consumer connection is closed.
    # name of queue can be read from result.method.queue
    result_queue = channel.queue_declare(queue='', exclusive=True)
    
    hello_queue = channel.queue_declare(queue='', exclusive=True)
    
    # bind the queue to the exchange: like a subscription to get incoming messages
    # in this case specify a routing_key: get only specific messages
    # we can bind the same queue to multiple exchanges with different routing keys, by calling queue_bind() multiple times
    channel.queue_bind(exchange='direct_logs',
                   queue=result_queue.method.queue,
                   routing_key='urgent')
    
    channel.queue_bind(exchange='direct_logs',
                   queue=hello_queue.method.queue,
                   routing_key='hello')

    def callback_urgent(ch, method, properties, body):
        print(f" [x] Received urgent: {body.decode()}")
        time.sleep(body.count(b'.') )
        print(" [x] Done")
        # ch.basic_ack(delivery_tag = method.delivery_tag)
        
    def callback_hello(ch, method, properties, body):
        print(f" [x] Received hello: {body.decode()}")
        print(" [x] Sending ack")
        ch.basic_ack(delivery_tag = method.delivery_tag)

    channel.basic_consume(queue=result_queue.method.queue, on_message_callback=callback_urgent, auto_ack=True)
    
    channel.basic_consume(queue=hello_queue.method.queue, on_message_callback=callback_hello)

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