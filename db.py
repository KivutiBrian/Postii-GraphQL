from orator import DatabaseManager, Schema, Model
from settings.config import settings

DATABASES = {
    "postgres": {
        "driver": settings.DRIVER,
        "host": settings.HOST,
        "database": settings.DATABASE,
        "user": settings.USER,
        "password": settings.PASSWORD,
        "prefix": "",
        "port": settings.PORT
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)