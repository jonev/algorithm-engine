import pika

class QueueService:
    def __init__(self, url) -> None:
        params = pika.URLParameters(url)
        params.socket_timeout = 5
        self.__connection = pika.BlockingConnection(params)
        self.__channel = self.__connection.channel()

    def close(self):
        self.__connection.close()
    
    def __callback(self, channel, method, properties, body):
        self.__on_message(body)

    def listen(self, on_message):
        self.__on_message = on_message
        self.__channel.basic_consume("jobs", self.__callback, auto_ack=True)
        self.__channel.start_consuming()
        self.close()