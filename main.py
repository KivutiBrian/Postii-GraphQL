import graphene
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schema import schema

from models.user import User

graphql_app = GraphQLRouter(schema)

app = FastAPI(
    title="FastAPI GraphQL"
)
app.include_router(graphql_app, prefix="/graphql")

@app.get('/')
def ping():
    return User.all()

