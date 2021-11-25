import logging
import signal
import sys

import config
from utils.logger import app_logger
from src.utils.control_utils.start import aiohttp_session
import bot


def main():
    setup()
    bot.start()


def setup():
    logging.basicConfig()
    app_logger.setLevel(config.logging_level())


# TODO handle SIGTERM refer to PomomoBeta
def handle_interrupt(signum, frame):
    # on_ready():
    #     restart_premium_sessions()
    print('Handling interrupt!', signum, frame)
    # Notify active session channels and persist premium sessions
    aiohttp_session.close()
    sys.exit(0)


if __name__ == '__main__':
    main()
