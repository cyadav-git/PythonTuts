from tkinter import *
from tkinter import Menu
from tkinter import messagebox
def openNewWindow():
    newWindow = Toplevel(win)
    newWindow.title("New Window")
    newWindow.geometry("200x200")
    Label(newWindow, text="This is the new opened window").pack()
def new():
    messagebox.showwarning("Alert", "Are you sure !!")


win = Tk()
win.minsize(300, 200)

win.title("Welcome to Menu Form")
menu = Menu(win)
#use to add the menu and tearoff is used to remove the dashed line from the menu
new_item = Menu(menu, tearoff=0)
#adds the new sub menu
new_item.add_command(label='New', command=openNewWindow)

#adds the separator to the menu list
new_item.add_separator()
new_item.add_command(label='File', command=new)
new_item.add_command(label='Setting')
new_item.add_separator()
new_item.add_command(label='Exit')
menu.add_cascade(label='File', menu=new_item)
win.config(menu=menu)
win.mainloop()