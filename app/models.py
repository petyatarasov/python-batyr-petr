from peewee import *

from config import db


class Product(Model):
    """
    Модель продукта с несколькими полями
        - Цена 
        - Название
        - Количество
        - Кнопка
    """

    price = IntegerField(
        verbose_name="Цена",
    )
    name = CharField(
        verbose_name="Название продукта",
        max_length=100
    )
    amount = IntegerField(
        verbose_name="Количество продукта в автомате",
    )
    button = IntegerField(
        verbose_name="Кнопка для выбора продукта",
    )


class Order(Model):
    """
    Модель заказа с несколькими полями
        - Продукт
        - Статус транзакции
    """

    product = ForeignKeyField(
        Product,
        backref="orders",
        verbose_name="Желаемый продукт",
    )
    transaction_status = CharField(
        verbose_name="Статус заказа"
    )


if __name__ == "__main__":
    db.connect()
    db.create_tables([Product, Order])
