from typing import List
from time import sleep

from fastapi import FastAPI, Depends

from dependencies import get_db, get_queue
from models import Product, Order
from schemas import ProductResponseSchema, ProductRequestSchema, ProductUpdateSchema, OrderRequestSchema, OrderResponseSchema
from tasks import show_hello
from tasks import sell_product

app = FastAPI(dependencies=[Depends(get_db)])

TIME_TO_SLEEP = 10


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/products")
def products() -> List[ProductResponseSchema]:
    """
    Отдает список всех продуктов из БД
    """

    #Достаем данные из базы
    product_list = Product.select()

    #превращаем в простые примитивы - список с диктом
    product_list_serialized = [ProductResponseSchema.from_orm(item) for item in product_list]

    return product_list_serialized

@app.get("/products/{pk}")
def get_product(pk: int) -> ProductResponseSchema:
    product = Product.get_by_id(pk)
    product_serialized = ProductResponseSchema.from_orm(product)

    return product_serialized

@app.post("/products")
def create_product(body: ProductRequestSchema) -> ProductResponseSchema:
    product = Product.create(
        price=body.price,
        name=body.name,
        amount=body.amount,
        button=body.button,
    )

    product_serialized = ProductResponseSchema.from_orm(product)

    return product_serialized

@app.patch("/products/{pk}")
def update_product(pk: int, body: ProductUpdateSchema) -> ProductResponseSchema:
    product = Product.get_by_id(pk)

    for key, value in body.dict(exclude_unset=True).items():
        setattr(product, key, value)


    product.save()

    response = ProductResponseSchema.from_orm(product)

    return response


@app.get("/sleep")
def make_sleep():
    sleep(TIME_TO_SLEEP)

    return {}

@app.delete("/products/{pk}")
def delete_product(pk: int) -> dict:
    product = Product.get_by_id(pk)
    product.delete_instance()

    return {}

@app.post("/run-task")
def run_task() -> dict:
    """
    endpoint for launch show_hello to message broker
    """

    queue = get_queue()
    queue.enqueue(show_hello, TIME_TO_SLEEP)

    return {}

@app.post("/orders")
def create_order(body: OrderRequestSchema) -> OrderResponseSchema:
    """
    prod and ts in the body
    """
    order = Order.create(
        #будут product_id, transaction_status и id
        product=body.product,
        transaction_status=body.transaction_status,
    )

    queue = get_queue()
    queue.enqueue(sell_product, order.id)

    order_serialized = OrderResponseSchema.from_orm(order)
    #OrderResponseSchema ждем поля prod, ts and id
    #Мы даем product, transaction_status and id

    return order_serialized

@app.post("/orders/{pk}")
def cancel_order(pk: int) -> OrderResponseSchema:
    order = Order.get_by_id(pk)
    order.transaction_status = "Cancel"

    order.save()

    response = OrderResponseSchema.from_orm(order)

    return response