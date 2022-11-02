from tkinter import *
from billorder import *

rootA = Toplevel()
rootA.title('testttt')
rootA.geometry('300x200')

L = Button(rootA, text='Test',command=CheckBill.command).pack()

rootA.mainloop()