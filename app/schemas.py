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

    @validator("age")
    def not_too_old(cls, value: int):
        if value >= AGE_OLD_LIMIT:
            raise ValueError("too-old-for-backend")

        return value


class ProductResponseSchema(ProductRequestSchema):
    """
    схема ответа от сервера [client <- back]
    """

    id: int

    class Config:
        orm_mode = True