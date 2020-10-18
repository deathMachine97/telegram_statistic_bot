from typing import NamedTuple, List
from data_structures.enum_classes import NotificationMode


class Notification(NamedTuple):
    _id: str
    time: str
    days: int


class StatisticsValue(NamedTuple):
    _id: str
    value: str
    date: str


class Notifications(NamedTuple):
    values: List[Notification]
    mode: NotificationMode


class Statistics(NamedTuple):
    _id: str
    name: str
    notification: list(Notification)
    notification_mode: NotificationMode
    user_id: int
    notify_text: str
    values: List[StatisticsValue]
    name: str
    strict_mode: bool
