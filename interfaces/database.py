from typing import List, NamedTuple, Optional, Dict, List, Tuple
from abc import ABC, abstractmethod
from threading import Lock, Thread
from interfaces.statistic import StatisticData, Statistic


class Database(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def init_connection(self) -> bool:
        pass

    @abstractmethod
    def create_statistic(self, data: StatisticData) -> bool:
        pass

    @abstractmethod
    def get_statistic(self, statistic_id: str) -> Statistic:
        pass

    @abstractmethod
    def get_notifications_to_send(self):
        pass

    
