import sqlite3
import hashlib

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );
    """
    try:
        c = conn.cursor()
        c.execute(create_users_table)
    except sqlite3.Error as e:
        print(e)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(conn, username, password):
    sql = ''' INSERT INTO users(username, password)
              VALUES(?,?) '''
    cur = conn.cursor()
    try:
        cur.execute(sql, (username, hash_password(password)))
        conn.commit()
        print(f"User {username} added successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")

def authenticate_user(conn, username, password):
    sql = ''' SELECT * FROM users WHERE username=? AND password=? '''
    cur = conn.cursor()
    cur.execute(sql, (username, hash_password(password)))
    rows = cur.fetchall()
    if rows:
        print("Authentication successful.")
        return True
    else:
        print("Authentication failed.")
        return False
