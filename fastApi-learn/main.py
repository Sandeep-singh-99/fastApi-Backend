from fastapi import FastAPI
from pydantic import BaseModel
from  typing import List

app = FastAPI()

class Tea(BaseModel):
    id: int
    name: str
    origin: str

teas: List[Tea] = []

@app.get("/tea")
async def read_tea():
    return {"Message": "Welcome to tea!"}

@app.get("/teas")
async def read_teas():
    return teas

@app.post("/teas")
async def add_tea(tea: Tea):
    teas.append(tea)
    return tea

@app.get("/teas/{tea_id}")
async def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return  updated_tea
    return {"error": "tea not found"}




@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def count_item(item_id: int):
    return {"item_id": item_id}



@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
