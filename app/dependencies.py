from fastapi import Depends


def show_hello():
    print("Hello")
    return {"a": 1, "b": 2}


def show_world(hello=Depends(show_hello)):
    print("World")
    return [1, 2, 3]