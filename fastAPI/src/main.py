from fastapi import FastAPI, HTTPException
from src import crud, db, models
from sqlalchemy.orm import Session
import aiosqlite

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await db.init_db()


@app.get("/users/")
async def get_users():
    async with aiosqlite.connect(db.database_url) as db_conn:
        cursor = await db_conn.execute("SELECT * FROM user")
        users = await cursor.fetchall()
        return users


@app.get("/user/{user_id}")
async def get_user(user_id: int):
    async with aiosqlite.connect(db.database_url) as db_conn:
        cursor = await db_conn.execute("SELECT * FROM user WHERE id = ?", (user_id,))
        user = await cursor.fetchone()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user


@app.get("/user/{user_id}/posts")
async def get_user_posts(user_id: int):
    async with aiosqlite.connect(db.database_url) as db_conn:
        cursor = await db_conn.execute("SELECT * FROM post WHERE user_id = ?", (user_id,))
        posts = await cursor.fetchall()
        if posts is None:
            raise HTTPException(status_code=404, detail="Post not found")
        return posts
