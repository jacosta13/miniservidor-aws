from fastapi import FastAPI

app = FastAPI(name="mini_server")


@app.get(path="/")
async def hello(a: int, b: int):
    return "hello, Mr Mojarras. ¿Cuantos pelos quiele hoy? " + str(a+b)

