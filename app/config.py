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
