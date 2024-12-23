from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/{item_id}")
def update_item(item_id: int, item: Item):
    price = item.price+18
    return {"item_id": item_id,"item_name": item.name,  "price":price}

@app.get("/calculator")
def calc(x: int,y: int,operator,task: Union[str, None] = None):
    if task:
        return {"Hello"}
    if operator == "+":
        return {"result":x+y}
    else:
        return {"result":x-y}    

class LoginRequest(BaseModel):
    user: str
    password: str
@app.post("/login")
def login(x:str,data: LoginRequest):
    if data.password == "hello":
        return {"message": "Login Success"}
    return {"message": "Failed, try again"} 
