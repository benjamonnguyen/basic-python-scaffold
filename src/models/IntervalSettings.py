from typing import Optional

from src import config


class IntervalSettings:

    def __init__(self,
                 pomodoro: Optional[int],
                 short_break: Optional[int],
                 long_break: Optional[int],
                 intervals: Optional[int]):
        self.pomodoro = pomodoro
        self.short_break = short_break
        self.long_break = long_break
        self.intervals = intervals
        if not self.is_valid():
            raise ValueError(f'IntervalSettings argument outside of range: 0-{config.max_interval_settings_value()}.')

    def is_valid(self) -> bool:
        max_val = config.max_interval_settings_value()
        if (self.pomodoro is None or 0 < self.pomodoro <= max_val) \
                and (self.short_break is None or 0 < self.short_break <= max_val) \
                and (self.long_break is None or 0 < self.long_break <= max_val) \
                and (self.intervals is None or 0 < self.intervals <= max_val):
            return True
        return False
