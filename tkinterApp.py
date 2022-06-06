from tkinter import *
def clicked():
    lbl.configure(text="The Button was clicked!!")
    res = "Welcome " + txt.get()
    lbl.configure(text=res)
window = Tk()
#to give the from title
window.title("Welcome to Nepal Airlines")
#use to place the logo on the form
window.iconbitmap("favicon.ico")
#the size of the window
#window.geometry("600x400")
#use to last minimize the window
window.minsize(300, 250)
#use to maximize the windows
window.maxsize(1200, 900)
#use to give the label in the frame
lbl = Label(window, text="Hello", font=("Arial Bold", 10))
lbl.grid(column=1, row=1)
lbl1 = Label(window, text="Welcome", font=("Arial Bold", 50))
lbl1.grid(column=2, row=2)
#textbox
txt = Entry(window, width=30)
txt.grid(column=3, row=3)
#use to make the button gb=backgraound color, fg= text color
btn = Button(window, text="Click Me", bg="orange", fg="red", command=clicked)
btn.grid(column=2, row=3)
#this mainloop is compulsary
window.mainloop()