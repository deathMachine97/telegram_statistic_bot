from typing import List, NamedTuple, Optional, Dict, List
from abc import ABC, abstractmethod
import typing
import enum


class NotifyTime(enum.Enum):
    Min = 'min'
    Hour = 'hour'
    Day = 'day'
    Week = 'week'
    Month = 'month'


class StatisticData(typing.NamedTuple):
    id: str
    user_id: int
    notify_time: NotifyTime
    notify_value: int


class Statistic(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get(self, statistic_id: str):
        pass

    @abstractmethod
    def create(self, data: StatisticData):
        pass

    @abstractmethod
    def update(self, statistic_id: str, new_value: StatisticData):
        pass

    @abstractmethod
    def delete(self, statistic_id: str):
        pass

    @abstractmethod
    def get_my_statistics_list(self, page: int = 0):
        pass
