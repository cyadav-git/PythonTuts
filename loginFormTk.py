import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
def click():
    username = username_entry.get()
    password = password_entry.get()
    if(username == 'admin' and password=='password'):
        messagebox.showinfo("Login Status", "user and password is matched")
    else:
        messagebox.showerror("Login Status", "the invalid login")

#root window
root = tk.Tk()
root.geometry("240x100")
root.title('Login')
root.resizable(0, 0)

#configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

#Username
username_lbl = ttk.Label(root, text="Username :")
username_lbl.grid(column=0, row=0, sticky=tk.W, padx=5,  pady=5)
username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

#password
password_lbl = ttk.Label(root, text="Password :")
password_lbl.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
password_entry = ttk.Entry(root, show="*")
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
#Login Button
login_btn = ttk.Button(root, text="Login", command=click)
login_btn.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

root.mainloop()