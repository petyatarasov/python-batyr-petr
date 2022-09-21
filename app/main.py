from fastapi import FastAPI, Depends

from dependencies import get_db
from models import Product


app = FastAPI(dependencies=[Depends(get_db)])


@app.get("/health")
def health():
    return {"status": "ti pidor"}


@app.get("/products")
def product():
    product_list = Product.select()
    product_list_serialized = [{
        "name": item.name
    } for item in product_list]

    return product_list_serialized