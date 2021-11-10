import logging
import signal
import sys

import uvloop

import config
from utils.logger import app_logger
from controller.control import aiohttp_session
import bot


def main():
    setup()
    bot.start()


def setup():
    uvloop.install()

    logging.basicConfig()
    app_logger.setLevel(config.logging_level())

    register_signals()


def register_signals():
    signal.signal(signal.SIGINT, handle_interrupt)
    signal.signal(signal.SIGTERM, handle_interrupt)


# TODO handle SIGTERM
def handle_interrupt(signum, frame):
    print('Handling interrupt!', signum, frame)
    aiohttp_session.close()
    sys.exit(0)


if __name__ == '__main__':
    main()
