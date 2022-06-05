import strawberry
from typing import List, Optional
from models.user import User as UserModel

# users=Us.all()

def all_users():
    return UserModel.all()


@strawberry.type
class User:
    id: strawberry.ID
    name: str
    address: str
    phone_number: str
    sex: str


@strawberry.type
class Query:
    # get all users
    users: Optional[List[User]] = strawberry.field(resolver=all_users)

    # get a user by id
    @strawberry.field
    def userById(self, userId:int) -> User:
        usr = UserModel.find_or_fail(userId)
        return usr


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user(self, name: str, address:str, phone_number: str, sex:str) -> User:
        usr = UserModel()
        usr.name = name
        usr.address = address
        usr.phone_number = phone_number
        usr.sex = sex
        usr.save()
        return usr


schema = strawberry.Schema(query=Query, mutation=Mutation)


