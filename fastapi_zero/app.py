from http import HTTPStatus

from fastapi import FastAPI

from fastapi_zero.schemas import (
    Message,
    UserDB,
    UserListSchema,
    UserPublicSchema,
    UserSchema,
)

app = FastAPI()


database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, Mundo!'}


@app.get('/users/', response_model=UserListSchema)
def read_users():
    return {'users': database}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublicSchema)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id
