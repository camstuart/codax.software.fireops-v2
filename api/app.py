from fastapi import FastAPI
from piccolo.engine import engine_finder

from database.tables import User

app = FastAPI()


@app.on_event("startup")
async def open_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.start_connection_pool()
    except Exception:
        print("! unable to connect to the database")


@app.on_event("shutdown")
async def close_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.close_connection_pool()
    except Exception:
        print("! unable to connect to the database")


@app.get("/")
async def root():
    users = await User.select().order_by(User.id)
    print(users)
    return {"message": "Hello World"}


@app.get("/users")
async def users_list():
    return await User.select().order_by(User.id)
