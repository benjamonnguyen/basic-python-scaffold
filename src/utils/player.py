from nextcord import PCMVolumeTransformer, FFmpegPCMAudio
from nextcord.voice_client import VoiceClient

from src.utils.logger import app_logger


def play(vc: VoiceClient, path: str, volume: float):
    # CLEANUP uncomment vc.play()
    audio = PCMVolumeTransformer(FFmpegPCMAudio(path, options='-loglevel error'),
                                 volume=volume)
    # vc.play(audio, after=lambda e: app_logger.error(f'Player error - path: {path}, guild: {vc.guild.name}, '
    #                                                 f'channel_id: {vc.channel.id}\n{e}') if e else None)

    app_logger.debug('Playing audio at ' + path)
