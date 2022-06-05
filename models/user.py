from orator.orm import has_many
# ensure our models use the config specified in db.py
from db import Model

class User(Model):

    __fillable__ = ['*']

    # specify a one to many relationship with posts
    @has_many
    def posts(self):
        from .post import Post
        return Post

    @has_many
    def comments(self):
        from .comment import Comments
        return Comments

