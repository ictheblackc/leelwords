import sqlite3
from tkinter import *
from tkinter import ttk


class Edit:
    """"""
    db_name = 'dictionary.db'

    def __init__(self, window):
        self.window = window
        self.window.title('Edit dictionary')
        #self.window.protocol('WM_DELETE_WINDOW', self.on_exit())

        self.right = Listbox(height=10)
        self.right.grid(row=0, column=0)


        self.left = Listbox(height=10)
        self.left.grid(row=0, column=1)


if __name__ == '__main__':
    root = Tk()
    root.geometry('320x320')
    app = Edit(root)
    root.mainloop()