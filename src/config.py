import yaml
import logging
from typing import List


def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


config = read_yaml('../config.yaml')
logging.info('Loaded config file for {} environment.'.format(config['APP']['ENVIRONMENT']))


def logging_level() -> int:
    return config['APP']['LOGGING_LEVEL']


def cmd_prefix() -> str:
    return config['BOT']['CMD_PREFIX']


def bot_token() -> str:
    return config['BOT']['TOKEN']


def authorized_user_ids() -> List[int]:
    return config['BOT']['AUTHORIZED_USER_IDS']


def chargebee_api_key() -> str:
    return config['CHARGEBEE']['API_KEY']


def cogs_path() -> str:
    return config['BOT']['COGS_PATH']


def max_interval_settings_value() -> int:
    return config['PARAMETER']['MAX_INTERVAL_SETTINGS_VALUE']


def rest_api_base_url() -> str:
    return config['REST_API']['BASE_URL']
