from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter.messagebox as tmsg
import pandas as pd
from tkinter.messagebox import showinfo
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
root=Tk()
root.geometry("1000x700")
def add():
    root.destroy()
    import Entrypage
    # Entrypage.root.destroy()
def disp():
    root.destroy()
    import Display
f1=ttk.LabelFrame(root,text="data").place(x=200,y=20,height=100,width=150)
f2=ttk.LabelFrame(root,text="display").place(x=10,y=20,height=100,width=150)
Button(f1,text="Add Item",command=add).pack()
Button(f2,text="Display Item",command=disp).pack()


can=Canvas(height=1000,width=1000)
can.pack()
can.create_line(0,30,1000,30)
img=ImageTk.PhotoImage(Image.open('p.ico'))
can.create_image(70,300,anchor=W,image=img)
root.mainloop()