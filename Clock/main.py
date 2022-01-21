# Tkinker is a common GUI to provide interfaces
# tkinker.tkk allows us tu use widgets

from tkinter import *
from tkinter.ttk import * 
from time import strftime

# GUI module 

root = Tk()
root.title("Clock")

def time():
    time_string = strftime('%H:%M:%S %p')
    label.config(text=time_string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor="center")
time()

mainloop()
