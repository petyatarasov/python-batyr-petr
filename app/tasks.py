from time import sleep
from models import Order


def show_hello(period: int):
    print("Hello")
    sleep(period)
    print("World")


def sell_product(pk: int):
    order = Order.get_by_id(pk)
    order.transaction_status = "Sell"

    order.save()

