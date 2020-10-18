from typing import List, NamedTuple, Optional, Dict, List, Tuple
from data_structures import tuple_classes
from interfaces import database


class Database(database.Database):
    def __init__(self):
        self.initail_connection()

    def init_connection(self) -> bool:
       cluster = MongoClient('')
       db = cluster['']
       self.db = db
       return True

    def create_statistics_object(self, statisttics_data) -> tuple_classes.statistics:
        return [
                '_id': str(statistics_data['_id']),
                'user_id' : int(statistics_data['user_id']),
                'notify_text': str(statistics_data['notify_text']),
                'name': str(statistics_data['name']),
                'strict_mode': bool(statistics_data['strict_mode'])
                ]

    """ Получает данные статистики """
    def get_statistics_info(self, statistic_id: str):
        statistics_collection = self.db['statistics']
        db_response = statistics_collection.aggregate([{
            '$match': {
                '_id': ObjectId(statistic_id)}
            }])
        result = [
                tuple_classes.Statistics(
                    _id = str(result['_id']),
                    name = str(result['name']),
                    notification = list( tuple_classes.Notification(
                                                _id = str(each_notification['_id']),
                                                time = each_notification['time'],
                                                days = int(each_notification['days'])
                                            ) notification for each_notification in result['notification']
                                        ),
                    notification_mode = str(result[''])
                    )
                for result in db_response
                
                ]
        return db_response

    """ Создает статистику """
    def create_statistics(self, data: tuple_classes.Statistics) -> bool:
        pass

    """ Обновляет параметры статистики """
    def update_statistics(self, statistic_id: str, new_value: tuple_classes.Statistics) -> bool:
        pass

    """ Удаляет статистику """
    def delete_statistics(self, statistic_id: str) -> bool:
        pass

    """ Возвращает списко созданных пользователем статистик"""
    def get_user_statistics(self, user_id: int, page: int = 0) -> tuple_classes.Statistics:
        pass

    """ Добавляет новую запись """
    def add_note_to_statistics(self, statistics_id: str, value) -> bool:
        pass

    """ Удаляет запись статистики """
    def delete_note_from_statistics(self, statistics_id: str, value_id: str) -> bool:
        pass

    """Получает последние записи статистики"""
    def get_last_notes_of_statistics(self, statistics_id: str, limit=30) -> List[tuple_classes.StatisticsValue]:
        pass

    """ Получает записи статистики """
    def get_notes_of_statistics(self, statistics_id: str, page=0) -> List[tuple_classes.StatisticsValue]:
        pass


