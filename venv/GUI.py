from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tmsg
from tkinter.messagebox import showinfo
root=Tk()

def show():
     print(" this is a box")
     tmsg._show("Error!!","There is some error in the code")
def info():
     val=tmsg.askquestion("How's your day","amazing or not")
     print(val)
# To change the title of the gui............................................
root.title("MY GUI")

# it sets the size of gui window...take input as "widthxheight".............
#root.geometry("200x300")

# to set the minimum size of window ........."width,height"..................
root.minsize(200,200)

# to set the maximum size of window ....."width,height"........................
#root.maxsize(600,500)

# to display something on the gui window.....................................
# t=Label(text='This is my first GUI window')
# t.pack()

# to display png images in the gui image,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# img=PhotoImage(file="photo.png")
# l=Label(image=img)
# l.pack()

# to display jpeg file.........................................................
# im=Image.open("new.jpeg")
# ph=ImageTk.PhotoImage(im)
# l=Label(image=ph)
# l.pack()

# Important label function.......................................................
# text-add the text
# bd-background
# fg-foreground
# font-chnage the font
# padx-x padding
# pady-y padding
# relief- styling border-SUNKEN,RAISED,GROOVE,RIDGE

#label=Label(text="hello my name is sumit mishra i am from india ", padx=20,pady=30,font="Arabic 20 bold",bg="light blue",fg="green",borderwidth=10,relief=SUNKEN)
# label.pack()

# Important pack function............................................................................
# anchor-sets direction like nw,ne,sw,se,s,n,e,wave
# side- sets the side top,bottom,left,right
# fill-
# padx
# pady

#label.pack(anchor="ne",side=BOTTOM,fill=X,padx=20,pady=20)

# Frames in gui..................................................................................
# f1=Frame(root,bg="light green",borderwidth=12,relief=SUNKEN)
# f1.pack(side=LEFT,fill=Y)
# l=Label(f1,text="GUI Frames")
# l.pack(fill=Y,pady=20)


# BUTTONS in GUI...............................................................
# def hello(event):
#      print(" Hello Developer!!!!!!!!!!!!!!!!!!")
# b1=Button(f1,text="Click",fg="green",command=hello)
# b1.pack(side=LEFT,anchor="nw")

# Variables in tkinter..........................................................
# BooleanVar,DoubleVar,IntVar,StringVar


# Grid and Entry field..................................................
# def getvalue():
#     print(uservalue.get())
#     print(passvalue.get())
#     # save data in a file......................................................
#     with open("record.txt","a") as f:
#         f.write(f"{uservalue.get(),passvalue.get(),ckvalue.get()}\n")
#
# user=Label(text=" Username")
# passw=Label(text="Password")
# user.grid()
# passw.grid(row=1)
#
# uservalue=StringVar()
# passvalue=StringVar()
# userentry=Entry(textvariable=uservalue)
# passentry=Entry(textvariable=passvalue)
# userentry.grid(row=0,column=1)
# passentry.grid(row=1,column=1)
#
# Button(text="Login",command=getvalue).grid(row=3)



# checkbox............................................................................
# ckvalue=IntVar()
# ck=Checkbutton(text=" I agree with terms and condition",variable=ckvalue).grid(row=2,column=1)


# Canvas in tkinter.........................................................................
# can=Canvas(width=400,height=400)
# can.pack()
# it takes two coordinate or 4 values like x1,y1,x2,y2
# can.create_line(0,10,100,10)
# it takes input as top left coordinates and bottom right coordinates
# can.create_rectangle(10,10,100,100)
# it takes input of rectangle
# can.create_oval(20,20,200,300)


# Events in tkinter.............................................................................
# wid=Button(text="click me")
# wid.pack()
# wid.bind('<Button-1>',hello)


# Menubar in tkinter..............................................................................
# mymenu=Menu(root)
# mymenu.add_command(label="file",command=hello)
# mymenu.add_command(label="exit",command=quit)
# root.config(menu=mymenu)

mainmenu=Menu(root)
m1=Menu(root,tearoff=0)
m1.add_command(label="new project",command=hello)
m1.add_command(label="open project",command=hello)
m1.add_command(label="save project",command=hello)
m1.add_separator()
m1.add_command(label="save as ",command=hello)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

# Dialog box.........................................................................
m2=Menu(root,tearoff=0)
m2.add_command(label="cut",command=hello)
m2.add_command(label="copy",command=hello)
m2.add_command(label="paste",command=info)
m2.add_separator()
m2.add_command(label="help ",command=show)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)


# slider in gui.......................................................................
# myslider=Scale(root,to=100,orient=HORIZONTAL).pack()


# Radiobutton.............................................................................
# l=Label(text="Is delhi is  a capital of India",padx=15).pack()
# val=IntVar()
# val.set(0)
# rd=Radiobutton(root,text="True",variable=val,value=1).pack(anchor="w")
# rd=Radiobutton(root,text="False",variable=val,value=2).pack(anchor="w")
# def res():
#      if val.get()==1:
#           tmsg._show("Result","Correct option")
#      else:
#           tmsg._show("Result","Wrorng opotion")
#
# b=Button(root,text="Submit",command=res).pack()

# Listbox ........................................................................

# def add():
#      global i
#      lb.insert(END,f"new element{i}")
#      i+=1
# i=1
# lb=Listbox(root)
# lb.pack()
# lb.insert(END,"First element")
# b=Button(text="Add",command=add ).pack()

# scrollbar...........................................................................
# widget(yscrollcommand=scroll.set)
# scrollbar.config(command=widget.yview)

# scb=Scrollbar(root)
# scb.pack(side=RIGHT,fill=Y)

# i=1
# lb=Listbox(root,yscrollcommand=scb.set)
# scb.config(command=lb.yview)
# lb.pack(anchor="w",fill=BOTH)
# lb.insert(END,"First element")
# b=Button(text="Add",command=add ).pack()

# Status bar...........................................
# def upload():
#      svar.set("wait......")
#      sbar.update()
#      import time
#      time.sleep(2)
#      svar.set("complied sucessfully")

# svar=StringVar()
# svar.set("Running...")
# sbar=Label(textvariable=svar,relief=RIDGE,anchor=W)
# sbar.pack(side=BOTTOM,fill=X)
# Button(text="Run",command=upload).pack()

# Change the icon of the gui.................................
# root.wm_iconbitmap("p.ico")

# root.configure(background="light blue")

# to close the window........................
# Button(text="Close",command=root.destroy).pack()


# Combobox............................................................


# Spinbox.............................................................

# LabelFrame..........................................................




root.mainloop()
