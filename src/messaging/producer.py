import pika

from src.messaging.messages.Message import Message
from src import config
from src.utils.logger import app_logger


_connection = pika.BlockingConnection(pika.URLParameters(config.mq_url()))
app_logger.info('Opened Producer connection.')
_control_channel = _connection.channel()
_control_channel.queue_declare(queue='control', durable=True)
app_logger.info('Opened Control channel.')


def send_control_message(message: Message):
    msgs = message.to_json()

    _control_channel.basic_publish(exchange='',
                                   routing_key='control',
                                   body=msgs,
                                   properties=pika.BasicProperties(delivery_mode=1))
    app_logger.debug(f'Sent Control message:\n{msgs}')
