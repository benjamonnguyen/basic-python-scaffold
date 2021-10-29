import logging
import signal
import sys
import os

import nextcord
from nextcord.ext import commands
import uvloop

import config
from commons.utils.logger import app_logger


def main():
    setup()
    start_bot()


def setup():
    uvloop.install()

    logging.basicConfig()
    app_logger.setLevel(config.logging_level())

    register_signals()


def start_bot():
    intents = nextcord.Intents(guilds=True,
                               reactions=True,
                               messages=True,
                               voice_states=True,
                               dm_messages=False,
                               dm_reactions=False)
    bot = commands.AutoShardedBot(command_prefix=config.cmd_prefix(),
                                  help_command=None,
                                  intents=intents)
    load_cogs(bot)

    @bot.event
    async def on_ready():
        app_logger.info(f'{bot.user} has connected to Discord!')
        app_logger.info(f'shard_count: {len(bot.shards)}')

    bot.run(config.bot_token())


def load_cogs(bot: commands.AutoShardedBot):
    for filename in os.listdir(config.cogs_path()):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
            app_logger.info(f'Loaded cogs.{filename[:-3]}')


def register_signals():
    signal.signal(signal.SIGINT, handle_interrupt)
    signal.signal(signal.SIGTERM, handle_interrupt)


# TODO handle SIGTERM
def handle_interrupt(signum, frame):
    print('Handling interrupt!', signum, frame)
    sys.exit(0)


if __name__ == '__main__':
    main()
