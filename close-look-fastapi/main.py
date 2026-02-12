import random
from typing import Annotated

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Create `tags_metadata` to provide better documentation
tags_metadata = [
    {
        "name": "Random Playground",
        "description": "Generate random numbers.",
    },
    {
        "name": "Random Items Management",
        "description": "Create, shuffle, read, update and delete items.",
    }
]

app = FastAPI(
    title="Randomizer API",
    description="Shuffle lists, pick random items, and generate random numbers.",
    version="1.0.0",
    openapi_tags=tags_metadata,
)

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://localhost:3000", "https://example.com"],
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    # Allowing all headers can expose API to security risks.
    #
    # In production,
    # - **Explicitly** list the headers allowed to access the API
    # - Use HTTPS for secure communication
    # - Carefully consider which HTTP methods and headers your API
    #   should accept from cross-origin requests
    #
    # allow_headers=["*"],
)

items_db = ["Clojure", "Python", "C#", "Java"]

class Item(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=100,
        description="The item name",
    )

# Response models

class ItemResponse(BaseModel):
    """Returning an Item."""
    message: str
    item: str


class ItemListResponse(BaseModel):
    original_order: list[str]
    randomized_order: list[str]
    count: int


class ItemUpdateResponse(BaseModel):
    message: str
    old_item: str
    new_item: str


class ItemDeleteResponse(BaseModel):
    message: str
    deleted_item: str
    remaining_items_count: int


@app.get("/", tags=["Random Playground"])
async def home():
    return {"message": "Welcome to the Randomizer API"}


@app.get("/random/{max_value}", tags=["Random Playground"])
async def get_random_number(max_value: int):
    """Generate a random number between 1 and max_value (inclusive)."""
    return {
        "max": max_value,
        "random_number": random.randint(1, max_value)
    }


@app.get("/random_between", tags=["Random Playground"])
async def get_random_number_between(
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


@app.get("/items", response_model=ItemListResponse,
         tags=["Random Items Management"])
async def get_randomized_items():
    randomized = items_db.copy()
    random.shuffle(randomized)
    return ItemListResponse(
        original_order=items_db,
        randomized_order=randomized,
        count=len(items_db),
    )


@app.post("/items", response_model=ItemResponse,
          tags=["Random Items Management"])
async def add_item(item: Item):
    if item.name in items_db:
        raise HTTPException(status_code=400, detail="Item already exists")

    items_db.append(item.name)
    return ItemResponse(
        message="Item added successfully",
        item=item.name,
    )


@app.put("/items/{update_item_name}", response_model=ItemUpdateResponse,
         tags=["Random Items Management"])
async def update_item(update_item_name: str, item: Item):
    if update_item_name not in items_db:
        raise HTTPException(status_code=404, detail=f"Item, '{update_item_name}', not found")

    if item.name in items_db:
        raise HTTPException(
            status_code=409,
            detail=f"An item with name, '{item.name}', already exists"
        )

    index = items_db.index(update_item_name)
    items_db[index] = item.name

    return ItemUpdateResponse(
        message="Item updated successfully",
        old_item=update_item_name,
        new_item=item.name
    )


@app.delete("/items/{item}", response_model=ItemDeleteResponse,
            tags=["Random Items Management"])
async def delete_item(item: str):
    if item not in items_db:
        raise HTTPException(status_code=404, detail=f"Item, '{item}', not found")

    items_db.remove(item)

    return ItemDeleteResponse(
        message="Item deleted successfully",
        deleted_item=item,
        remaining_items_count=len(items_db)
    )
