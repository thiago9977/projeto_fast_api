from fastapi import FastAPI

from http import HTTPStatus

from projeto_fast_api.schemas import Message

app = FastAPI()


@app.get('/', status_code= HTTPStatus.OK, response_model= Message)
def root():
    return {'message': 'italo é o juliusip'}
