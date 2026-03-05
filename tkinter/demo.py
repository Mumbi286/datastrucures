#  Tkinter - A special library in python to build graphical user interfaces using python
from tkinter import *
# Adding two numbers
def add():
    n1 = int(number1.get())
    n2 = int(number2.get())
    result = str(n1+n2)
    answer.config(text="Answer is: "+ result)

root = Tk()
root.geometry("300x300")

number1 = Entry(root)
number2 = Entry(root)
number1.pack()
number2.pack()

button = Button(root, text='Add', command=add)
button.pack()

answer = Label(root)
answer.pack()

root.mainloop()