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
