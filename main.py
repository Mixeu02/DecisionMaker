from tkinter import *
from random import randint

root = Tk()
root.title("Decision Maker")
root.geometry("400x400")

num1 = 1
num2 = 2

def decide():
    decision = randint(1, 2)
    if decision == 1:
        Label1.config(fg="green")
        Label2.config(fg="red")
    else:
        Label1.config(fg="red")
        Label2.config(fg="green")

Label1 = Label(root, text=num1, font="Arial, 50")
Label2 = Label(root, text=num2, font="Arial, 50")
Button1 = Button(root, text="Decide", font="Arial, 10", command=decide)

Label1.place(relx=0.35, rely=0.5, anchor=CENTER)
Label2.place(relx=0.65, rely=0.5, anchor=CENTER)
Button1.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()