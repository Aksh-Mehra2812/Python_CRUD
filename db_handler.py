# db_handler.py
import sqlite3

DATABASE_FILE = "crud_app.db"

def create_table():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    """)
    connection.commit()
    connection.close()

def insert_item(name, description):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO items (name, description) VALUES (?, ?)", (name, description))
    connection.commit()
    connection.close()

def get_all_items():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    connection.close()
    return items

def update_item(item_id, name, description):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("UPDATE items SET name=?, description=? WHERE id=?", (name, description, item_id))
    connection.commit()
    connection.close()

def delete_item(item_id):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM items WHERE id=?", (item_id,))
    connection.commit()
    connection.close()
