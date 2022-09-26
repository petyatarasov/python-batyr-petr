from peewee import *
from environs import Env
from redis import Redis


env = Env()
env.read_env()

DATABASE_NAME = env("DATABASE_NAME")
DATABASE_URL = env("DATABASE_URL")

REDIS_URL = env("REDIS_URL")


def get_db():
    """
    зависиость, которая возвращает соединение с бд
    """

    db = PostgresqlDatabase(
        database=DATABASE_NAME,
        dsn=DATABASE_URL,
    )
    db.connect()

    return db

def get_redis():
    """
    возвращает соед с редис 
    """

    redis = Redis.from_url(url=REDIS_URL)

    return redis

def get_redis():
    redis = Redis.from_url(url=REDIS_URL)

    return redis

def get_queue():
    redis = get_redis()
    queue = Queue(connection=redis)

    return queue
