from enum import IntEnum, auto


class Event(IntEnum):
    pass


class ProducerEvent(Event):
    START = auto()
    END = auto()


class ConsumerEvent(Event):
    SEND_MESSAGE = auto()
    EDIT_MESSAGE = auto()
    PLAY_AUDIO = auto()
