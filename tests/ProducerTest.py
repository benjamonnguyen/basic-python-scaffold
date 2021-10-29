import unittest
import logging

from commons.utils.logger import app_logger
from src.messaging import producer


class ProducerTest(unittest.TestCase):
    logging.basicConfig()
    app_logger.setLevel(logging.DEBUG)

    def test_send_start_message(self):
        from src.messaging.messages.StartMessage import StartMessage
        from src.models.IntervalSettings import IntervalSettings
        msg = StartMessage(0, IntervalSettings(25, 5, 10, 4))
        producer.send_control_message(msg)


if __name__ == '__main__':
    unittest.main()
