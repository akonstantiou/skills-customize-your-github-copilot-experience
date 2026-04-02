"""Starter code for the FastAPI REST APIs assignment.

Run locally:
    pip install fastapi uvicorn
    uvicorn starter-code:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Assignment Starter")


class ItemCreate(BaseModel):
    name: str
    description: str


items = []


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment starter."}


@app.get("/items")
def list_items():
    return {"items": items}


@app.post("/items", status_code=201)
def create_item(item: ItemCreate):
    next_id = len(items) + 1
    record = {
        "id": next_id,
        "name": item.name,
        "description": item.description,
    }
    items.append(record)
    return record


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
