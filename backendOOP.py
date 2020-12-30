import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("bookstore.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(" CREATE TABLE IF NOT EXISTS  books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn TEXT)")
        self.connection.commit()
        # self.connection.close()

    def insert(self, title, author, year, isbn):
        self.cursor.execute(" INSERT INTO books VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.connection.commit()
        # self.connection.close()

    def view(self):
        self.cursor.execute(" SELECT * FROM books")
        allBooks = self.cursor.fetchall()
        # self.connection.close()
        return allBooks

    def search(self, title='', author='', year='', isbn=''):
        # passing empty strings as default values to the arguments of the search method
        self.cursor.execute(" SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        theBook = self.cursor.fetchall()
        # self.connection.close()
        return theBook

    def delete(self, id):
        self.cursor.execute("DELETE FROM books WHERE id=?", (id,))
        self.connection.commit()
        # self.connection.close()

    def update(self, id, title, author, year, isbn):
        self.cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.connection.commit()
        # self.connection.close()




# insert('The Sun', 'Jane Doe', 1957, 288384738220032)
# print(search(author='John Smith'))
# delete(3)
# update(3, 'The Sun', 'Jane Smith', 1954, 425251626535252)
# print(view())