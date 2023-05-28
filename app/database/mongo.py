"""
This file contents the connection to the database
"""
from app.utility import utils
from pymongo import MongoClient


DATABASE_URL = utils.getenv('DATABASE_URL')
DATABASE_NAME = utils.getenv('DATABASE_NAME')


def __get_database() -> MongoClient:
    client = MongoClient(DATABASE_URL)

    return client[DATABASE_NAME]


database = __get_database()
