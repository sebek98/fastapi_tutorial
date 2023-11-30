from typing import Union
import uvicorn

from fastapi import FastAPI
from models import Item, ModelName, MojaData, external_data


app = FastAPI()


@app.get("/")
async def main():
    return {"data": "Hello world!"}


@app.get("/blogs")
async def blogs():
    return MojaData(**external_data)


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


@app.get("/items")
async def create_items(item: Item = Item()):
    return item


@app.get("/items/{item_id}")
async def get_item(item_id: str, q: Union[int, None] = None, short: bool = False):
    item = {"data": item_id}
    if q:
        return item.update({"q": q})
    if not short:
        item.update({"description": "Jakis tam description, zobaczymy jak to wyjdzie.!?"})
    return item

@app.get("/items/{item_id}/ja")
async def get_item_item(item_id: str, needy: str):
    return {"data": item_id, "needy": needy}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
