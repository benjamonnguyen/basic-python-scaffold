from typing import Dict, Optional

from models import Timer
from utils.logger import app_logger


_cache: Dict[int, Timer] = {}


def insert(channel_id: int, timer: Timer):
    if get(channel_id) is None:
        _cache[channel_id] = timer
        app_logger.info(f'Inserted timer for channel_id: {channel_id}.')
    else:
        raise ValueError(f'Timer already exists for channel_id: {channel_id}.')


def delete(channel_id: int):
    if get(channel_id) is not None:
        del _cache[channel_id]
        app_logger.info(f'Deleted timer for channel_id: {channel_id}.')
    else:
        raise KeyError(f'Channel_id {channel_id} not found.')


def get(channel_id: int) -> Optional[Timer]:
    return _cache.get(channel_id)
