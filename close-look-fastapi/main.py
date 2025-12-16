import random

from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def read_main():
    return {'message': 'Welcome to the Randomizer API'}

@app.get('/random/{max_value}')
def get_random_number(max_value: int):
    return {
        'max': max_value,
        'random_number': random.randint(1, max_value),
    }
