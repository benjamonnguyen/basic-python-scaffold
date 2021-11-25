import asyncio
from typing import Dict
import json
import random

import aiohttp
from nextcord.ext.commands.context import Context
from nextcord.message import Message

from src.utils import player
from src.utils.logger import app_logger
from src.enums import Link, AudioPath
from src import config, timer_manager
from src.models.Timer import Timer

GREETINGS = ['Howdy howdy! Let\'s do this thang.',
             'Hey there! Let\'s get started!',
             'It\'s productivity o\'clock!',
             'Let\'s ketchup on some work!']

aiohttp_session = aiohttp.ClientSession(config.rest_api_base_url(), loop=asyncio.get_event_loop())


async def start(ctx: Context, payload: str):
    try:
        resp = await aiohttp_session.post('/session/start', json=payload)
        if resp.status == 409:
            asyncio.create_task(ctx.send('There is already a session in this channel.'))
            app_logger.debug(f'Session already exists for channel: {ctx.channel.name} (409)')
        else:
            resp.raise_for_status()
        json_obj = await resp.json()
        interval_settings = json_obj.get('interval_settings')

        msg = await _send_start_msg(ctx, interval_settings)
        asyncio.create_task(_play_start_audio(ctx))
        timer_manager.insert(ctx.channel.id, Timer(interval_settings.get('pomodoro'), msg))

        # queue_transition_request()

    except (aiohttp.ClientResponseError, KeyError) as e:
        asyncio.create_task(ctx.send('There seems to be a problem on the backend. Please try again later.\n\n'
                                     'If the problem persists, notify @Support in the support server!\n' + Link.SUPPORT))
        app_logger.critical(f'Bad response for start request: {json.dumps(payload, indent=4)}\n{e}')


# TODO message_builder.start_message()
async def _send_start_msg(ctx: Context, json_obj) -> Message:
    # await cleanup.pins(session)
    msg = await ctx.send(random.choice(GREETINGS) + '\n{}')
                         # embed=msg_builder.timer_status_embed(session, start=True))
    # await asyncio.gather(ctx.send(embed=msg_builder.settings_embed(session)), msg.pin())
    return msg


async def _play_start_audio(ctx: Context):
    vc = await ctx.author.voice.channel.connect()
    player.play(vc, AudioPath.POMO_START, 5.0)
    await ctx.send('Playing audio!')
