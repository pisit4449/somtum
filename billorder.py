
from tkinter import *
from tkinter import ttk, messagebox

class CheckBill:

    def __init__(self):
        pass


    def popup(self):
        rootCB = Toplevel()
        rootCB.geometry('800x500')
        rootCB.iconbitmap('images/dog.ico')
        rootCB.title('Check Bill')

        L = Label(rootCB, text='Test').pack()

        rootCB.mainloop()

    def command(self):
        self.popup()

CheckBill.command