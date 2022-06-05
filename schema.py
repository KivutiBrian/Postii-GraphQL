import strawberry
from typing import List, Optional
from models.user import User as UserModel
from models.post import Post as PostModel

# users=Us.all()

def all_users():
    return UserModel.with_('posts').get()


@strawberry.type
class Post:
    title: str
    body: str

@strawberry.type
class User:
    id: strawberry.ID
    name: str
    address: str
    phone_number: str
    sex: str


@strawberry.type
class PostWithAuthor:
    title: str
    body: str
    user: User


@strawberry.type
class UserWithPosts:
    id: strawberry.ID
    name: str
    address: str
    phone_number: str
    sex: str
    posts: Optional[List[Post]]



@strawberry.type
class Query:
    # get all users
    users: Optional[List[UserWithPosts]] = strawberry.field(resolver=all_users)

    # get a user by id
    @strawberry.field
    def userById(self, userId:int) -> UserWithPosts:
        usr = UserModel.with_('posts').find_or_fail(userId)
        return usr

    @strawberry.field
    def postById(self, postId: int) -> Post:
        pst = PostModel.find_or_fail(postId)
        return pst


@strawberry.type
class Mutation:

    # add new user
    @strawberry.mutation
    def add_user(self, name: str, address:str, phone_number: str, sex:str) -> UserWithPosts:
        usr = UserModel()
        usr.name = name
        usr.address = address
        usr.phone_number = phone_number
        usr.sex = sex
        usr.save()
        return usr

    # add post
    @strawberry.mutation
    def add_post(self, userId: int, title: str, body: str) -> PostWithAuthor:
        pst = PostModel()
        pst.user_id = userId
        pst.title = title
        pst.body = body
        pst.save()
        return pst
    

schema = strawberry.Schema(query=Query, mutation=Mutation)


