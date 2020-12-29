import sqlite3

def db_connection():
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute(" CREATE TABLE IF NOT EXISTS  books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn TEXT)")
    connection.commit()
    connection.close()

def insert(title, author, year, isbn):
    connection = sqlite3.connect("bookstore.db")
    cursor.connection.cursor()0
    cursor.execute(" INSERT INTO books VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute(" SELECT * FROM books")
    allBooks = cursor.fetchall()
    connection.close()
    return allBooks