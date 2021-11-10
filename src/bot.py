import os

from nextcord import Intents
from nextcord.ext.commands import AutoShardedBot

import config
from utils.logger import app_logger


def start():
    bot = AutoShardedBot(command_prefix=config.cmd_prefix(),
                         help_command=None,
                         intents=_get_intents())
    _load_cogs(bot)

    @bot.event
    async def on_ready():
        app_logger.info(f'{bot.user} has connected to Discord!')
        app_logger.info(f'shard_count: {len(bot.shards)}')

    bot.run(config.bot_token())


def _load_cogs(bot):
    for filename in os.listdir(config.cogs_path()):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
            app_logger.info(f'Loaded cogs.{filename[:-3]}')


def _get_intents() -> Intents:
    return Intents(guilds=True,
                   reactions=True,
                   messages=True,
                   voice_states=True,
                   dm_messages=False,
                   dm_reactions=False)
