from fastapi import FastAPI, Query

from pydantic import BaseModel
from typing import Annotated


class Item(BaseModel):
    price: int
    desc: str | None = None
    to: str
    tax: int | None =  None


app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = ['foo', 'bar']):
    query_items = {'q': q}
    
    return query_items