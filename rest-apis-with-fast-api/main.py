from fastapi import FastAPI, HTTPException
from mongita import MongitaClientDisk
from pydantic import BaseModel


class Shape(BaseModel):
    name: str
    no_of_sides: int
    id: int


app = FastAPI()


client = MongitaClientDisk()
db = client.db
shapes = db.shapes

# Populate our "database"
shapes.insert_one({"name": "triangle", "no_of_sides": 3, "id": 1})

# Find all documents in our "database" (that is, **an empty filter**)
shapes.find({})




@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/shapes")
async def get_shapes():
    all_shapes = shapes.find({})
    return [
        # Removes the `_id` field from the shape. This field is inserted by
        # Mongita because it **cannot** be automatically translated to JSON.
        {key: shape[key] for key in shape if key != "_id"} for shape in all_shapes
    ]


@app.get("/shapes/{shape_id}")
async def get_shape_by_id(shape_id: int) -> dict[str, str | int] | None:
    if shapes.count_documents({"id": shape_id}) > 0:
        shape = shapes.find_one({"id": shape_id})
        return {key: shape[key] for key in shape if key != "_id"}

    raise HTTPException(status_code=404,
                        detail=f"Shape with id, {shape_id}, not found.")


@app.post("/shapes")
async def create_shapes(shape: Shape):
    # Video passes `shape.dict()`; however, when I pass this, PyCharm
    # "crosses out" the `dict()` method with information that `dict()`
    # is not obsolete and should be replaced with `model_dump`.
    shapes.insert_one(shape.model_dump())
    return shape
