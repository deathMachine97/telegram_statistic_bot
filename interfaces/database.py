from typing import List, NamedTuple, Optional, Dict, List, Tuple
from abc import ABC, abstractmethod
from threading import Lock, Thread
from data_structures import tuple_classes


class Database(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def init_connection(self) -> bool:
        pass

    """ Получает данные статистики """
    @abstractmethod
    def get_statistics_info(self, statistic_id: str):
        pass

    """ Создает статистику """
    @abstractmethod
    def create_statistics(self, data: tuple_classes.Statistics):
        pass

    """ Обновляет параметры статистики """
    @abstractmethod
    def update_statistics(self, statistic_id: str, new_value: tuple_classes.Statistics):
        pass

    """ Удаляет статистику """
    @abstractmethod
    def delete_statistics(self, statistic_id: str):
        pass

    """ Возвращает списко созданных пользователем статистик"""
    @abstractmethod
    def get_user_statistics(self, user_id: int, page: int = 0):
        pass

    """ Добавляет новую запись """
    @abstractmethod
    def add_note_to_statistics(self, statistics_id: str, value) -> bool:
        pass

    """ Удаляет запись статистики """
    @abstractmethod
    def delete_note_from_statistics(self, statistics_id: str, value_id: str) -> bool:
        pass

    """Получает последние записи статистики"""
    @abstractmethod
    def get_last_notes_of_statistics(self, statistics_id: str, limit=30) -> List[tuple_classes.StatisticsValue]:
        pass

    """ Получает записи статистики """
    @abstractmethod
    def get_notes_of_statistics(self, statistics_id: str, page=0) -> List[tuple_classes.StatisticsValue]:
        pass
