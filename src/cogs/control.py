import asyncio

from nextcord.ext import commands

from src.models.IntervalSettings import IntervalSettings
from src import config
from src.controller import control
from src.utils.serializer import serialize


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
        if ctx.author.voice is None or ctx.author.voice.channel is None:
            asyncio.create_task(ctx.send('Please join a voice channel and try again!'))
            return
        try:
            asyncio.create_task(ctx.send('Starting session...'))
            payload = serialize({
                'channel_id': ctx.channel.id,
                'voice_channel_id': ctx.author.voice.channel.id,
                'interval_settings': IntervalSettings(pomodoro, short_break, long_break, intervals)
            })
            asyncio.create_task(control.start(ctx, payload))
        except ValueError:
            asyncio.create_task(ctx.send(f'Use numbers between 0 and {config.max_interval_settings_value()}.'))


def setup(client):
    client.add_cog(Control(client))
