from enum import Enum
from typing import Union
from pydantic import BaseModel

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class MojaData(BaseModel):
    data: dict


external_data = {
    "data":
        {
            "1": "blog 1",
            "2": "blog 2",
            "3": "blog 3",
            "4": "blog 4",
            "5": "blog 5",
        }
    }