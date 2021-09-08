
from tkinter import *
root1 = Tk()

def myclick():
    mylabel5 = Label(root1, text="look i clicked here")
    mylabel5.grid(row=3, column = 3)

def myclick2():
    root = Tk()
    
    mylabel5 = Label(root1, text="look i clicked here from butto2")
    mylabel5.grid(row=4, column = 4)
    root.mainloop

    

    
e1= Entry(root1, width=50)
e2=Entry(root1, width=50)
e3=Entry(root1, width=50)
e4=Entry(root1, width=50)
    
    
mylabel1 = Label(root1, text="Name")
mylabel2 = Label(root1, text="address")
m3 = Label(root1, text="age")
m4 = Label(root1, text="phn")

button1 = Button(root1, text="button1 click here",command=myclick, fg="black", bg="yellow")
button2 = Button(root1, text="button2 here", command=myclick2)

mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=0)
button1.grid(row=2, column=2)
button2.grid(row=2, column=3)
m3.grid(row=2,column=0)
m4.grid(row=3,column=0)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)


root1.mainloop()
