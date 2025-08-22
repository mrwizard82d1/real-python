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
# Commented out now that we can populate our database using typical
# web requests.
# shapes.insert_one({"name": "triangle", "no_of_sides": 3, "id": 1})

# Find all documents in our "database" (that is, **an empty filter**)
# shapes.find({})


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


@app.put("/shapes/{shape_id}")
async def update_shape(shape_id: int, shape: Shape):
    if shapes.count_documents({"id": shape_id}) > 0:
        shapes.replace_one({"id": shape_id}, shape.model_dump())
        return shape
    raise HTTPException(status_code=404, detail=f"Shape with id, {shape_id}, not found.")


@app.put("/shapes/upsert/{shape_id}")
async def upsert_shape(shape_id: int, shape: Shape):
    # An "upsert" will update a document if it exists already; otherwise, it
    # will insert a **new** document
    shapes.replace_one({"id": shape_id}, shape.model_dump(), upsert=True)
    return shape


@app.delete("/shapes/{shape_id}")
async def delete_shape(shape_id: int):
    delete_result = shapes.delete_one({"id": shape_id})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404,
                            detail=f"Shape with id, {shape_id}, not found to delete.")
    return {"OK": True}
