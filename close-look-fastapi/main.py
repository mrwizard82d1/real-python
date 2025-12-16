from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def read_main():
    return {'message': 'Welcome to the Randomizer API'}
