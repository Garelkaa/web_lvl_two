import aiosqlite

DATABASE_URL = "../database.db"
database_url = "sqlite:///" + DATABASE_URL


async def init_db():
    async with aiosqlite.connect(database_url) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY,
                email TEXT,
                gender TEXT,
                status TEXT
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS post (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                title TEXT,
                body TEXT,
                FOREIGN KEY (user_id) REFERENCES user (id)
            )
        ''')
        await db.commit()
