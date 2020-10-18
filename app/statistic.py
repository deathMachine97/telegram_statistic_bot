from typing import List, NamedTuple, Optional, Dict, List
from interfaces import statistic
from data_structures import tuple_classes


class Statistics(statistic.Statistics):
    def __init__(self):
        pass

    """ Получает данные статистики """

    def get(self, statistic_id: str):
        pass

    """ Создает статистику """
    def create(self, data: tuple_classes.Statistic):
        pass

    """ Обновляет параметры статистики """

    def update(self, statistic_id: str, new_value: tuple_classes.Statistics):
        pass

    """ Удаляет статистику """
    def delete(self, statistic_id: str):
        pass

    """ Возвращает спискок созданных пользователем статистик"""
    def get_user_statistics(self, user_id: int, page: int = 0):
        pass

    """ Добавляет новую запись """
    def add_note(self, statistics_id: str, value) -> bool:
        pass

    """ Удаляет запись статистики """
    def delete_note(self, statistics_id: str, value_id: str) -> bool:
        pass

    """Получает последние записи статистики"""
    def get_last_notes_of_statistics(self, statistics_id: str, limit=30) -> List[tuple_classes.StatisticsValue]:
        pass

    """ Получает записи статистики """
    def get_statistics_notes(self, statistics_id: str, page=0) -> List[tuple_classes.StatisticsValue]:
        pass
