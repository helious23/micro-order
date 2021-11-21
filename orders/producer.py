import os
import pika
import json

params = pika.URLParameters(os.environ.get("AMQP_URL"))

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange="",
        routing_key="restaurant",
        body=json.dumps(body),
        properties=properties,
    )
