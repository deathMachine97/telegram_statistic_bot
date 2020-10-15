from typing import NamedTuple, List
from data_structures.enum_classes import NotificationMode


class StatisticsValue(NamedTuple):
    id: str
    value: str
    date: str


class Notification(NamedTuple):
    id: str
    time: str
    days: int

class NotificationCollection(NamedTuple):
    time: List[str]
    mode: NotificationMode


class Statistics(NamedTuple):
    id: str
    notification: NotificationCollection
    user_id: int
    notify_text: str
    values: List[StatisticsValue]
    name: str
    strict_mode: bool
