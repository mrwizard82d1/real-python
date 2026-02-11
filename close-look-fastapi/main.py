import random
from typing import Annotated

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

app = FastAPI()

items_db = ["Clojure", "Python", "C#", "Java"]

class Item(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=100,
        description="The item name",
    )


@app.get("/random_between")
def get_random_number_between(
        min_value: Annotated[int, Query(
            title="Minimum value",
            description="The minimum random number",
            ge=1,
            le=1000
        )] = 1,
        max_value: Annotated[int, Query(
            title="Maximum value",
            description="The maximum random number",
            ge=1,
            le=1000
        )] = 99
):
    if min_value > max_value:
        raise HTTPException(status_code=400,
                            detail=f"Minimum value, {min_value}, "
                                   f"cannot be greater than maximum value, {max_value}.")

    return {
        "min": min_value,
        "max": max_value,
        "random_number": random.randint(min_value, max_value),
    }


@app.get("/")
async def home():
    return {"message": "Welcome to the Randomizer API"}


@app.get("/random/{max_value}")
def get_random_number(max_value: int):
    """Generate a random number between 1 and max_value (inclusive)."""
    return {
        "max": max_value,
        "random_number": random.randint(1, max_value)
    }


@app.get("/items")
def get_randomized_items():
    randomized = items_db.copy()
    random.shuffle(randomized)
    return {
        "original_order": items_db,
        "randomized_order": randomized,
        "count": len(items_db),
    }


@app.post("/items")
def add_item(item: Item):
    # Remove the initialization and validation of `item_name`:
    # item_name = body.get("name")
    # if not item_name:
    #     raise HTTPException(status_code=400, detail="'name' field is required")

    if item.name in items_db:
        raise HTTPException(status_code=400, detail="Item already exists")

    items_db.append(item.name)
    return {"message": "Item added successfully",
            "item": item.name}


@app.put("/items/{update_item_name}")
def update_item(update_item_name: str, body: dict):
    if update_item_name not in items_db:
        raise HTTPException(status_code=404, detail=f"Item, '{update_item_name}', not found")

    new_name = body.get("name")
    if not new_name:
        raise HTTPException(
            status_code=400,
            detail="'name' field is required in request body",
        )

    if new_name in items_db:
        raise HTTPException(
            status_code=409,
            detail=f"An item with name, '{new_name}', already exists"
        )

    index = items_db.index(update_item_name)
    items_db[index] = new_name

    return {
        "message": "Item updated successfully",
        "old_item": update_item_name,
        "new_item": new_name
    }


@app.delete("/items/{item}")
def delete_item(item: str):
    if item not in items_db:
        raise HTTPException(status_code=404, detail=f"Item, '{item}', not found")

    items_db.remove(item)

    return {
        "message": "Item deleted successfully",
        "deleted_item": item,
        "remaining_items_count": len(items_db)
    }
