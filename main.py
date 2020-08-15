from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(name="mini_server")


class Inputs(BaseModel):
    number_1: int
    number_2: int
    name: str


@app.get(path="/")
async def hello(a: int, b: int):
    return "hello, Mr Mojarras. ¿Cuantos pelos quiele hoy? " + str(a+b)


@app.post(path="/post-path")
async def hello_post(request: Inputs):
    pelos = request.number_1 * request.number_2
    return f"Hello, {request.name}: You have {pelos} Pelos!"
