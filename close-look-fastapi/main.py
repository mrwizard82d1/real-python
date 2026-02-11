import random
from typing import Annotated

from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

items_db = ["Clojure", "Python", "C#", "Java"]


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
def add_item(body: dict):
    item_name = body.get("name")
    if not item_name:
        raise HTTPException(status_code=400, detail="'name' field is required")

    if item_name in items_db:
        raise HTTPException(status_code=400, detail="Item already exists")

    items_db.append(item_name)
    return {"message": "Item added successfully",
            "item": item_name}
