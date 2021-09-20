
from tkinter import *
root = Tk()
mylabel1 = Label(root, text="00")
mylabel2 = Label(root, text="01")



m3 = Label(root, text="10")
m4 = Label(root, text="11")
#m1.pack()
#m2.pack()


mylabel1.grid(row=0,column=0)
mylabel2.grid(row=0,column=1)
m3.grid(row=1, column=0)
m4.grid(row=1, column=1)

root.mainloop()
