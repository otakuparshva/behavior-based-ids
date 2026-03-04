import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
    """)

    # Insert default users
    cursor.execute("INSERT OR IGNORE INTO users VALUES ('admin', 'admin123')")
    cursor.execute("INSERT OR IGNORE INTO users VALUES ('user1', 'password1')")

    conn.commit()
    conn.close()


def validate_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()

    conn.close()
    return result is not None