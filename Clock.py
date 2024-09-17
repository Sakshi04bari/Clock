from tkinter import Tk
from tkinter import Label
import time 
import sys

master = Tk()
master.title("Digital Clock")



#make a function which update each second
def get_time():
    timeVar=time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)
clock = Label(master, font=("Calibri",90),bg="grey",fg="black")
clock.pack()

get_time()

master.mainloop()
