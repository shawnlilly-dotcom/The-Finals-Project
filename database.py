import sqlite3
from pathlib import Path

DATABASE = Path(__file__).resolve().parent / "gamevault.db"


def create_database():
    with sqlite3.connect(DATABASE) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                genre TEXT,
                platform TEXT,
                status TEXT DEFAULT 'Not Started',
                rating INTEGER
            )
        """)


def add_game(title, genre, platform, status):
    with sqlite3.connect(DATABASE) as connection:
        connection.execute(
            "INSERT INTO games (title, genre, platform, status) VALUES (?, ?, ?, ?)",
            (title, genre, platform, status),
        )


def get_games():
    with sqlite3.connect(DATABASE) as connection:
        return connection.execute(
            "SELECT id, title, genre, platform, status FROM games ORDER BY id DESC"
        ).fetchall()


if __name__ == "__main__":
    create_database()
    print("GameVault database created successfully!")
