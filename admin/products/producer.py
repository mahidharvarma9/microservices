import pika, json

#params = pika.URLParameters('amqps://oenwuqee:91pzsvj2f941LHWu7ZY0-L9D5ojQ_v1K@snake.rmq2.cloudamqp.com/oenwuqee?heartbeat=65535')

#connection = pika.BlockingConnection(params)

#channel = connection.channel()


def publish(method, body):
    params = pika.URLParameters('amqps://oenwuqee:91pzsvj2f941LHWu7ZY0-L9D5ojQ_v1K@snake.rmq2.cloudamqp.com/oenwuqee?heartbeat=65535')
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
