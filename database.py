
import sqlite3

DATABASE = "gamevault.db"


def create_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT,
            platform TEXT,
            status TEXT DEFAULT 'Not Started'
        )
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()
    print("GameVault database created successfully!")
