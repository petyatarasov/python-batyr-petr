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