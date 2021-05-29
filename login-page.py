from tkinter import *
from tkinter import Toplevel
from tkinter import Tk, Menu
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk



global m
global e1
global e2
global names
global passes
names = ['mahir','jeevan','keerthikashri','shanmuga','venu']
passes = [123,1234]

def about():
    messagebox.showinfo("About Us","Team Infernos-Cicada 3301: Reinvented")

def openNewWindow():


        username = str(e1.get())
        


        if username == "":
            messagebox.showinfo("Alert","Enter username")
            

        
        else:
            if username in names:
            
                password = e2.get()
                password = int(password)
                if password in passes:
                    newWindow = Toplevel(win)
                    newWindow.title("New Window")

                    

#front end

'''code below
'''
'''
# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

# creates a Tk() object
master = Tk()

# sets the geometry of main
# root window
master.geometry("200x200")


# function to open a new window
# on a button click
def openNewWindow():
	
	# Toplevel object which will
	# be treated as a new window
	newWindow = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	newWindow.title("New Window")

	# sets the geometry of toplevel
	newWindow.geometry("200x200")

	# A Label widget to show in toplevel
	Label(newWindow,
		text ="This is a new window").pack()


label = Label(master,text ="This is the main window")

label.pack(pady = 10)

# a button widget which will open a
# new window on button click
btn = Button(master,text ="Click to open a new window",
command = openNewWindow)
btn.pack(pady = 10)

# mainloop, runs infinitely
'''
'''
code above
'''

'''
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

'''    

win=tk.Tk()

win.geometry("500x300")
win.title("Virtual Notes")

#menu bar
menu_bar= Menu(win)
#submenu
'''
fileMenu = Menu(menu_bar, tearoff=0)


fileMenu.add_command(label="exit", command=win.destroy)
fileMenu.add_command(label="kill", command=win.destroy)
fileMenu.add_command(label="stop", command=win.destroy)

menu_bar.add_cascade(label="File", menu=fileMenu)
win.config(menu=menu_bar)

'''
'''
code below
'''

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

 
'''
code above
'''
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

submit = Button(win, text = "Submit", command=openNewWindow)
submit.place(x=210,y=200)
    
win.mainloop()

    















