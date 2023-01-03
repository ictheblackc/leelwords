import sqlite3
import os
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class App:
    """"""
    db_name = 'dictionary.db'

    def __init__(self, window):
        self.window = window
        self.window.title('leelwords')

        Button(text='Edit', command=self.on_edit).pack(side='bottom', fill='x')
        Button(text='Restart', command=self.on_restart).pack(side='bottom', fill='x')

        self.left = Listbox()
        self.left.bind('<<Listbox>>', self.left_callback)
        self.left.pack(side='left', fill='both', expand=True)

        self.right = Listbox()
        self.right.bind('<<Listbox>>', self.right_callback)
        self.right.pack(side='right', fill='both', expand=True)

        #self.window.protocol('WM_DELETE_WINDOW', self.on_exit())

        self.get_words()

    def on_exit(self):
        """Action on exit"""
        if messagebox.askyesno('Exit', 'Exit program?'):
            self.window.destroy()

    def on_restart(self):
        """"""

    def on_edit(self):
        """"""
        os.system('python edit.py')

    def get_words(self):
        """Fill lists with words"""
        query = 'SELECT * FROM dictionary ORDER BY word DESC'
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            result = cursor.execute(query)
            connection.commit()
            right_list = []
            left_list = []
            for row in result:
                right_list.append(row[1])
                left_list.append(row[2])
            random.shuffle(right_list)
            random.shuffle(left_list)
            dictionary = dict(zip(right_list, left_list))
            for key, value in dictionary.items():
                self.left.insert(END, key)
                self.left.insert(END, value)

    def right_callback(self):
        """Right list handler"""
        pass

    def left_callback(self):
        """Right list handler"""
        pass


if __name__ == '__main__':
    root = Tk()
    root.geometry('640x640')
    app = App(root)
    root.mainloop()
