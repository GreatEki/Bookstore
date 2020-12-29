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

window = Tk()

# Label
titleLabel = Label(window, text='Title')
titleLabel.grid(row=0, column=0)


AuthorLabel = Label(window, text='Author')
AuthorLabel.grid(row=0, column=2)


YearLabel = Label(window, text='Year')
YearLabel.grid(row=1, column=0)

IsbnLabel = Label(window, text='ISBN')
IsbnLabel.grid(row=1, column=2)

# End of Labels

# Creating Entries
# Entries are similar to textbox in html
title_text = StringVar()
titleEntry = Entry(window, textvariable=title_text)
titleEntry.grid(row=0, column=1)

author_text = StringVar()
authorEntry = Entry(window, textvariable=author_text)
authorEntry.grid(row=0, column=3)

year_text = StringVar()
yearEntry = Entry(window, textvariable=year_text)
yearEntry.grid(row=1, column=1)

isbn_text = StringVar()
isbnEntry = Entry(window, textvariable=isbn_text)
isbnEntry.grid(row=1, column=3)

# Create ListBox
bookList = Listbox(window, height=6)
bookList.grid(row=2, column=0, rowspan=6, columnspan=2)

# Create Scroll Bar
bookScroll = Scrollbar(window)
bookScroll.grid(row=2, column=2, rowspan=6)

bookList.configure(yscrollcommand=bookScroll.set)
bookScroll.configure(command=bookList.yview)


# Create Buttons
ViewBtn = Button(window, text='View All', width=12)
ViewBtn.grid(row=2, column=3)

SearchBtn = Button(window, text='Search All', width=12)
SearchBtn.grid(row=3, column=3)

AddBtn = Button(window, text='Add Entry', width=12)
AddBtn.grid(row=4, column=3)

updateBtn = Button(window, text='Update', width=12)
updateBtn.grid(row=5, column=3)

deleteBtn = Button(window, text='Delete', width=12)
deleteBtn.grid(row=6, column=3)

CloseBtn = Button(window, text='Close', width=12)
CloseBtn.grid(row=7, column=3)


window.mainloop()