from fastapi import FastAPI

from enum import Enum


app = FastAPI()


class Item(str, Enum):
    wtf = 'wtf'
    qqq = 'qqq'
    www = 'www'


@app.get('/')
async def root():
    return {
        "message": "Hello world"
    }


@app.get('/items/{item_name}')
async def read_item(item_name: Item):
    if item_name is Item.wtf:
        return {
            'item_name': item_name,
            'message': 'And why?',
        }
    if item_name is Item.www:
        return {
            'item_name': item_name,
            'message': 'www?',
        }
    return {
        'item_name': item_name,
        'message': 'You trash//',
    }