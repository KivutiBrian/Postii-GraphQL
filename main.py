from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schema import schema

from models.user import User

graphql_app = GraphQLRouter(schema)

app = FastAPI(
    title="FastAPI GraphQL"
)
app.include_router(graphql_app, prefix="/graphql")

from pydantic import BaseModel
from typing import List, Optional

class Post(BaseModel):
    title: str
    body: str

class Users(BaseModel):
    id: int
    name: str
    address: str
    phone_number: str
    sex: str
    posts: Optional[List[Post]]

    class Config:
        orm_mode = True


@app.get('/',
# response_model=List[Users]
)
def ping():
    # return User.with_('posts').first().to_dict()
    return User.with_('posts').get()
