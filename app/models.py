from peewee import *

from dependencies import get_db


db = get_db()


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
        max_length=100,
    )
    amount = IntegerField(
        verbose_name="Количество продукта в автомате",
    )
    button = IntegerField(
        verbose_name="Кнопка для выбора продукта",
    )

    class Meta:
        database = db


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

    class Meta:
        database = db

