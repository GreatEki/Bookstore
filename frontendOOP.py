"""
A program that stores books information:
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close

"""


from tkinter import *
from backendOOP import Database

database= Database()

class client(object):
    def __init__(self, window):
        self.window = window
        # Add Window Title
        window.wm_title("Bookstore")
    
        # Label
        titleLabel = Label(window, text='Title')
        titleLabel.grid(row=0, column=0)


        AuthorLabel = Label(window, text='Author')
        AuthorLabel.grid(row=0, column=2)


        YearLabel = Label(window, text='Year')
        YearLabel.grid(row=1, column=0)

        IsbnLabel = Label(window, text='ISBN')
        IsbnLabel.grid(row=1, column=2)

        # Creating Entries
        # Entries are similar to textbox in html
        self.title_text = StringVar()
        self.titleEntry = Entry(window, textvariable=self.title_text)
        self.titleEntry.grid(row=0, column=1)

        self.author_text = StringVar()
        self.authorEntry = Entry(window, textvariable=self.author_text)
        self.authorEntry.grid(row=0, column=3)

        self.year_text = StringVar()
        self.yearEntry = Entry(window, textvariable=self.year_text)
        self.yearEntry.grid(row=1, column=1)

        self.isbn_text = StringVar()
        self.isbnEntry = Entry(window, textvariable=self.isbn_text)
        self.isbnEntry.grid(row=1, column=3)

        # End of Labels

        # Create ListBox
        self.bookList = Listbox(window, height=6)
        self.bookList.grid(row=2, column=0, rowspan=6, columnspan=3)

        # Create Scroll Bar
        bookScroll = Scrollbar(window)
        bookScroll.grid(row=2, column=3, rowspan=6)

        self.bookList.configure(yscrollcommand=bookScroll.set)
        bookScroll.configure(command=self.bookList.yview)

        # Bind Listbox Widget to a function
        self.bookList.bind('<<ListboxSelect>>', self.get_selected_book)

        # Create Buttons
        ViewBtn = Button(window, text='View All', width=12, command=self.view_books)
        ViewBtn.grid(row=2, column=4)

        SearchBtn = Button(window, text='Search All', width=12, command=self.search_book)
        SearchBtn.grid(row=3, column=4)

        AddBtn = Button(window, text='Add Entry', width=12, command=self.add_book)
        AddBtn.grid(row=4, column=4)

        updateBtn = Button(window, text='Update', width=12, command=self.update_book)
        updateBtn.grid(row=5, column=4)

        deleteBtn = Button(window, text='Delete', width=12, command=self.delete_book)
        deleteBtn.grid(row=6, column=4)

        CloseBtn = Button(window, text='Close', width=12, command=window.destroy)
        CloseBtn.grid(row=7, column=4)
    
        
    def get_selected_book(self, event):
        try:
            global selected_book
            # We get the index of the item on the list box
            index = self.bookList.curselection()[0]
            # We need to get the content of the selected item in the listbox using the index
            selected_book = self.bookList.get(index)

            # Pasting the values of selected book in the Entry Widget
            self.titleEntry.delete(0, END)
            self.titleEntry.insert(END, selected_book[1])

            self.authorEntry.delete(0, END)
            self.authorEntry.insert(END, selected_book[2])

            self.yearEntry.delete(0, END)
            self.yearEntry.insert(END, selected_book[3])

            self.isbnEntry.delete(0, END)
            self.isbnEntry.insert(END, selected_book[4])
        except IndexError:
            pass

    def view_books(self):
        self.bookList.delete(0, END)
        # We are emptying the list box before displaying the list of books
        for row in database.view():
            self.bookList.insert(END, row)

    def search_book(self):
        self.bookList.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.bookList.insert(END, row)

    def add_book(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.bookList.delete(0, END)
        self.bookList.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))


    def delete_book(self):
        database.delete(selected_book[0])


    def update_book(self):
        database.update(selected_book[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()) 

        

window = Tk()
client(window)
window.mainloop()