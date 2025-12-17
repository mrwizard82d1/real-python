import random
from typing import Annotated

from fastapi import FastAPI, HTTPException, Query


app = FastAPI()


# A (cheap) in-memory database
items = []


@app.get('/')
def read_main():
    return {'message': 'Welcome to the Randomizer API'}

# Declare path and query parameters with types
@app.get('/random/{max_value}')
def get_random_number(max_value: int):
    return {
        'max': max_value,
        'random_number': random.randint(1, max_value),
    }

# Add query parameters
@app.get('/random-between')
def get_random_number_between(
        min_value: Annotated[int, Query(
            title='Minimum Value',
            description='The minimum random number',
            ge=1,
            le=1000
        )] = 1,
        max_value: Annotated[int, Query(
            title="Maximum Value",
            description='The maximum random number',
            ge=1,
            le=1000
        )] = 99,
):
    if min_value > max_value:
        raise HTTPException(status_code=400,
                            detail="min_value cannot be greater than max_value")

    return {
        'min': min_value,
        'max': max_value,
        'random_number': random.randint(min_value, max_value)
    }
