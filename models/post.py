from orator.orm import has_many
# ensure our models use the config specified in db.py
from db import Model

class Post(Model):

    @has_many
    def comments(self):
        from .comment import Comments
        return Comments
