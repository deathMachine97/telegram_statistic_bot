from typing import List, NamedTuple, Optional, Dict, List
from abc import ABC, abstractmethod

from data_structures.tuple_classes import StatisticsData, StatisticsValue, StatisticsList


class Statistics(ABC):
    @abstractmethod
    def __init__(self):
        pass

    """ Получает данные статистики """
    @abstractmethod
    def get(self, statistic_id: str):
        pass

    """ Создает статистику """
    @abstractmethod
    def create(self, data: StatisticsData):
        pass

    """ Обновляет параметры статистики """
    @abstractmethod
    def update(self, statistic_id: str, new_value: StatisticsData):
        pass

    """ Удаляет статистику """
    @abstractmethod
    def delete(self, statistic_id: str):
        pass

    """ Возвращает списко созданных пользователем статистик"""
    @abstractmethod
    def get_user_statistics(self, user_id: int, page: int = 0):
        pass

    """ Добавляет новую запись """
    @abstractmethod
    def add_note(self, statistics_id: str, value) -> bool:
        pass

    """ Удаляет запись статистики """
    @abstractmethod
    def delete_note(self, statistics_id: str, value_id: str) -> bool:
        pass

    """Получает последние записи статистики"""
    @abstractmethod
    def get_last_notes_of_statistics(self, statistics_id: str, limit=30) -> List[StatisticsValue]:
        pass

    """ Получает записи статистики """
    @abstractmethod
    def get_statistics_notes(self, statistics_id: str, page=0) -> List[StatisticsValue]:
        pass

