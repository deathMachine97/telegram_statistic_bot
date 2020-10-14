from time import sleep
import datetime as dt

from abc import ABC, abstractmethod

from typing import Dict, List, NamedTuple
from interface.statistic import StatisticData, Statistic
from interface.database import Database
from interface.statistic import StatisticData

class Notification(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_notifications_to_send(self) -> List[StatisticData]:
        pass

    @abstractmethod
    def send_notification(self, data: StatisticData):
        pass


"""
now_time = dt.datetime.now()

while True:
    delta_minutes = dt.datetime.now() - now_time
    if delta_minutes.seconds >= 60:
        
        now_time = dt.datetime.now()

    break

"""
