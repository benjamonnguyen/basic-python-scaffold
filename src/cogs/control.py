import asyncio

from nextcord.ext import commands

from src import config
from src.utils.serializer import serialize
from src.utils.validator import validate_interval_settings
from src.utils import control_utils


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

        asyncio.create_task(ctx.send('Starting session...'))
        intervals_settings = {
            'pomodoro': pomodoro,
            'short_break': short_break,
            'long_break': long_break,
            'intervals': intervals
        }
        validate_interval_settings(intervals_settings)
        payload = serialize({
            'channel_id': ctx.channel.id,
            'voice_channel_id': ctx.author.voice.channel.id,
            'interval_settings': intervals_settings
        })

        asyncio.create_task(control_utils.start(ctx, payload))

    @start.error
    async def handle_error(self, ctx: commands.Context, e: commands.CommandError):
        if isinstance(e, ValueError):
            asyncio.create_task(ctx.send(f'Use numbers between 0 and {config.max_interval_settings_value()}.'))


def setup(client):
    client.add_cog(Control(client))
