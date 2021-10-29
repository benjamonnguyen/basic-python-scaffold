from .Message import Message
from src.enums.event_enums import ProducerEvent
from src.models.IntervalSettings import IntervalSettings


class StartMessage(Message):
    def __init__(self,
                 channel_id: int,
                 interval_settings: IntervalSettings):
        self.channel_id = channel_id
        self.interval_settings = interval_settings
        self.control_event_name = ProducerEvent.START.name
