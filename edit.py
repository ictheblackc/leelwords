import sqlite3
from tkinter import *
from tkinter import ttk


class Edit:
    """"""
    db_name = 'dictionary.db'

    def __init__(self, window):
        self.window = window
        self.window.title('Edit dictionary')

        self.message = Label(text='', fg='green')
        self.message.grid(row=3, column=0, columnspan=2)

        frame = LabelFrame(self.window, text='Add a new word')
        frame.grid(row=0, column=0, columnspan=2, pady=10)

        self.word = Entry(frame)
        self.word.focus()
        self.word.grid(row=1, column=1)

        self.meaning = Entry(frame)
        self.meaning.grid(row=2, column=1)

        self.tree = ttk.Treeview(height=10, column=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Word')
        self.tree.heading('#1', text='Meaning')

        Button(text='Add', command=self.add_word).grid()
        Button(text='Edit', command=self.edit_word).grid()
        Button(text='Delete', command=self.delete_word).grid()

        self.get_words()

    def get_words(self):
        """"""
        rows = self.tree.get_children()
        for row in rows:
            self.tree.delete(row)
        query = 'SELECT * FROM dictionary ORDER BY word DESC'
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            result = cursor.execute(query)
            connection.commit()
            for row in result:
                self.tree.insert('', 0, text=row[1], values=row[2])

    def add_word(self):
        """"""
        if self.validate():
            query = 'INSERT INTO dictionary VALUES(NULL, ?, ?)'
            parameters = (self.word.get(), self.meaning.get())
            with sqlite3.connect(self.db_name) as connection:
                cursor = connection.cursor()
                result = cursor.execute(query, parameters)
                connection.commit()
            self.message['text'] = 'Word {} has been added to the dictionary'
            self.word.delete(0, END)
            self.meaning.delete(0, END)
        else:
            self.message['text'] = 'Enter word and its meaning'
        self.get_words()

    def delete_word(self):
        """"""

    def edit_word(self):
        """"""

    def validate(self):
        """"""
        return len(self.word.get()) != 0 and len(self.meaning.get()) != 0

if __name__ == '__main__':
    root = Tk()
    root.geometry('320x320')
    app = Edit(root)
    root.mainloop()