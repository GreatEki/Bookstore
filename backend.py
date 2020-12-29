import sqlite3

def db_connection():
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute(" CREATE TABLE IF NOT EXISTS  books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn TEXT)")
    connection.commit()
    connection.close()

def insert(title, author, year, isbn):
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
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

def search(title='', author='', year='', isbn=''):
    # passing empty strings as default values to the arguments of the search method
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute(" SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    theBook = cursor.fetchall()
    connection.close()
    return theBook

def delete(id):
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (id,))
    connection.commit()
    connection.close()

def update(id, title, author, year, isbn):
        connection = sqlite3.connect("bookstore.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        connection.commit()
        connection.close()

db_connection()

# insert('The Sun', 'Jane Doe', 1957, 288384738220032)
# print(search(author='John Smith'))
# delete(3)
# update(3, 'The Sun', 'Jane Smith', 1954, 425251626535252)
# print(view())