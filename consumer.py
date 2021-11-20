import os
import pika
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

params = pika.URLParameters(os.environ.get("AMQP_URL"))

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="order")


def callback(ch, method, properties, body):
    print("Received in order")
    print(body)


channel.basic_consume(queue="order", on_message_callback=callback)

print("Started consuming")

channel.start_consuming()

channel.close()
