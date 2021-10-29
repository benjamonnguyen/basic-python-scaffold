import pika

from src.messaging.messages.Message import Message
from src import config
from src.utils.logger import app_logger

QUEUE = 'SESSION_CONTROL'
_connection = pika.BlockingConnection(pika.URLParameters(config.mq_url()))
app_logger.info('Opened Producer connection.')
_control_channel = _connection.channel()
_control_channel.queue_declare(queue=QUEUE, durable=True)
app_logger.info(f'Opened {QUEUE} channel.')


def send_control_message(message: Message):
    msgs = message.to_json()

    _control_channel.basic_publish(exchange='',
                                   routing_key=QUEUE,
                                   body=msgs,
                                   properties=pika.BasicProperties(
                                       headers={'message_type': message.__class__.__name__},
                                       delivery_mode=1
                                   ))
    app_logger.debug(f'Sent {message.__class__.__name__} to {QUEUE} queue:\n{msgs}')
