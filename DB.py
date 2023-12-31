"""TODO: реализовать подключение к базе +добавление элементов + удаление всех элементов"""
from pymongo import MongoClient


def mongo_connect():
    """Подключаемся к БД"""
    client = MongoClient('localhost', 27017)
    db = client.test_data
    coll = db.test2
    return coll


collbd = mongo_connect()


def mongo_add_data(args: dict):
    """Добавляем в документ данные. Кормить только словарями!"""
    try:
        collbd.insert_one(args)
    except TypeError:
        print("Document must be an instance of dict")


def mongo_removal_all_data():
    """Удаление всех записей из документа"""
    collbd.delete_many({})


def mongo_find_first_one(args: dict):
    """Ищем первого подходящего. Кормить только словарями!"""
    return collbd.find_one(args)


def mongo_find_and_update(old_data: dict, new_data: dict):
    """Возвращает первую подходящую запись и меняем ее значения"""
    res = mongo_find_first_one(old_data)
    collbd.update_one(old_data, {"$set": new_data})
    return res


mongo_find_and_update({"not_told": "true"}, {"not_told": "folse"})