from fastapi import FastAPI, Depends

from dependencies import show_world


app = FastAPI()


@app.get("/health")
def health(world=Depends(show_world)):
    return {"status": "ti pidor"}
