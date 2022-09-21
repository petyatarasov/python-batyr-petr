from fastapi import Depends


def show_hello():
    print("Hello")
    return {"a": 1, "b": 2}


def show_world(hello=Depends(show_hello)):
    print("World")
    return [1, 2, 3]

from peewee import *
from environs import Env


env = Env()
env.read_env()

DATABASE_NAME = env("DATABASE_NAME")
DATABASE_DSN = env("DATABASE_DSN")


db = PostgresqlDatabase(
    database=DATABASE_NAME,
    dsn=DATABASE_DSN,
)


def get_db():
    """
    зависиость, которая возвращает соединение с бд
    """

    db = postgresqlDatabase(
        database=DATABASE_NAME,
        dsn=DATABASE_DSN,
    )
    db.connect()

    return db