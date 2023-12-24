from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine


DB = PostgresEngine(
    config={
        "database": "fireops-unified-v2",
        "user": "postgres",
        "password": "password",
        "host": "localhost",
        "port": 5432,
    }
)


# A list of paths to piccolo apps
# e.g. ['blog.piccolo_app']
APP_REGISTRY = AppRegistry(apps=["database.piccolo_app"])
