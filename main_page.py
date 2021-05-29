from tkinter import *
from tkinter import Toplevel
from tkinter import Tk, Menu
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from recognition_module import recorder



global m
global e1
global e2
global names
global passes
password = 0
names = ['mahir','jeevan','keerthikashri','shanmuga','venu']
passes = [123,1234]


def page1(win):
    page = tk.Frame(win)
    page.grid()
    submit = Button(win, text = "Submit", command=changepage)
    submit.place(x=210,y=200)


def page2(win):
    page = tk.Frame(win)
    page.grid()
    tk.Label(page, text = 'This is page 2').grid(row = 0)
    record = Button(win, text = "Record", command = recorder)
    record.place(x=210,y=120)
    

def changepage():
    global pagenum, win

    username = str(e1.get())
    if username != "":
        password = int(e2.get())
    
    if username == "":
        messagebox.showinfo("Alert","Enter username")
    else:
        if username!="" and password!=0:
            if password in passes:
                for widget in win.winfo_children():
                    widget.destroy()
                if pagenum == 1:
                    page2(win)
                    pagenum=0
    
    
def about():
    messagebox.showinfo("About Us","Team Infernos-Cicada 3301: Reinvented")

win=tk.Tk()

win.geometry("500x300")
win.title("Virtual Notes")

#menu bar
menu_bar= Menu(win)

#submenu

file = Menu(menu_bar, tearoff=0)  
file.add_command(label="New")  
file.add_command(label="Open")  
file.add_command(label="Save")  
file.add_command(label="Save as...")  
file.add_command(label="Close")  
  
file.add_separator()  
  
file.add_command(label="Exit", command=win.quit)  
  
menu_bar.add_cascade(label="File", menu=file)  
edit = Menu(menu_bar, tearoff=0)  
edit.add_command(label="Undo")  
  
edit.add_separator()  
  
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
edit.add_command(label="Delete")  
edit.add_command(label="Select All")  
  
menu_bar.add_cascade(label="Edit", menu=edit)  
help = Menu(menu_bar, tearoff=0)  
help.add_command(label="About", command=about)  
menu_bar.add_cascade(label="Help", menu=help)  
  
win.config(menu=menu_bar)  

 

#page 1 accessories

login_label = Label(win, text = "Login", fg="blue",
                    font = ("Poppins", 15)).place(x=210,y=50)

name = Label(win, text = "Name :")
name.place(x=150,y=100)
e1 = Entry(win)
e1.place(x=220,y=100)
password = Label(win, text = "Password :")
password.place(x=132,y=150)
e2 = Entry(win)
e2.place(x=220,y=150)



#calling the function of first page    
page1(win)
pagenum = 1

win.mainloop()

    















