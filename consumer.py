import os
import django
import json
import pika
from dotenv import load_dotenv, find_dotenv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from orders import models

load_dotenv(find_dotenv())

params = pika.URLParameters(os.environ.get("AMQP_URL"))

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="order")


def callback(ch, method, properties, body):
    print("Received in order")
    print(body)
    if properties.content_type == "order_deliver_finished":
        id = json.loads(body)
        order = models.Order.objects.get(pk=id)
        order.deliver_finithed = True
        order.save()
        print("order deliver finished")


channel.basic_consume(queue="order", on_message_callback=callback, auto_ack=True)

print("Started consuming")

channel.start_consuming()

channel.close()
