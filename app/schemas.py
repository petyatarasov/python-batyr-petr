from typing import Optional
from pydantic import BaseModel, validator


class ProductRequestSchema(BaseModel):
    """
    схема запроса данных на сервер [client -> back]
    """

    price: int
    name: str
    amount: int
    button: int

    class Config:
        orm_mode = True

class ProductResponseSchema(ProductRequestSchema):
    """
    схема ответа от сервера [client <- back]
    """

    id: int

    class Config:
        orm_mode = True


class ProductUpdateSchema(BaseModel):
    """
    схема запроса данных для обновления на сервер [client -> back]
    """

    price: Optional[int]
    name: Optional[str]
    amount: Optional[int]
    button: Optional[int]

    class Config:
        orm_mode = True