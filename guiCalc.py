from tkinter import *
from tkinter import messagebox
def clicked():
    num1 = int(txt1.get())
    num2 = int(txt2.get())
    sum1 = num1+num2
    #messagebox.showinfo('the sum is: ', sum1)
    lbl.configure(text=sum1)
win = Tk()
win.title("Calculator")
win.minsize(200, 200)
lbl1 = Label(win, text="Enter First Number", font=("Arial Bold", 15))
lbl1.grid(column=2,row=1)
txt1 = Entry(win, width=30)
txt1.grid(column=2, row=2)
lbl2 = Label(win, text="Enter second Number", font=("Arial Bold", 15))
lbl2.grid(column=2,row=3)
txt2 = Entry(win, width=30)
txt2.grid(column=2, row=4)
btn = Button(win, text="Calculate", bg="yellow", fg="red", command=clicked)
btn.grid(column=2, row=5)
lbl = Label(win, text="")
lbl.grid(column=2, row=6)

win.mainloop()