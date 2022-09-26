from typing import List
from time import sleep

from fastapi import FastAPI, Depends

from dependencies import get_db
from models import Product
from schemas import ProductResponseSchema, ProductRequestSchema

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

@app.get("/sleep")
def make_sleep():
    sleep(TIME_TO_SLEEP)

    return {}

@app.delete("/products/{pk}")
def delete_product(pk: int) -> dict:
    product = Product.get_by_id(pk)
    product.delete_instance()

    return {}
