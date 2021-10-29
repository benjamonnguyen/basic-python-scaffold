import asyncio

from nextcord.ext import commands

from src.models.IntervalSettings import IntervalSettings
from src.messaging import producer
from src.messaging.messages.StartMessage import StartMessage
from src import config


class Control(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def start(self,
                    ctx: commands.Context,
                    pomodoro: int = None,
                    short_break: int = None,
                    long_break: int = None,
                    intervals: int = None):
        try:
            interval_settings = IntervalSettings(pomodoro, short_break, long_break, intervals)
            producer.send_control_message(StartMessage(ctx.channel.id, interval_settings))
        except ValueError:
            asyncio.create_task(ctx.send(f'Use numbers between 0 and {config.max_interval_settings_value()}.'))
