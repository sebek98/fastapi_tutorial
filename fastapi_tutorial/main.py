from typing import Union

from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"



app = FastAPI()


@app.get("/")
async def main():
    return {"data": "Hello world!"}


@app.get("/blogs")
async def blogs():
    return {"data":
        {
            "1": "blog 1",
            "2": "blog 2",
            "3": "blog 3",
            "4": "blog 4",
            "5": "blog 5",
        }
    }


@app.get("/blogs/{id}")
async def blog(id: int):
    return {"data": {f"{id}": f"blog {id}"}}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "HAve some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.get("/items/{item_id}")
async def get_item(item_id: str, q: Union[int, None] = None, short: bool = False):
    item = {"data": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "Jakis tam description, zobaczymy jak to wyjdzie.!?"})
    return item

@app.get("/items/{item_id}/ja")
async def get_item_item(item_id: str, needy: str):
    return {"data": item_id, "needy": needy}

