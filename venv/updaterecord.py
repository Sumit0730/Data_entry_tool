from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter.messagebox as tmsg
import pandas as pd
from tkinter.messagebox import showinfo

root = Tk()
# root.maxsize(1000, 900)
root.minsize(1500,1600)
root.geometry("1366x768")
root.title("Data Visualization")
root.configure(background="#4C787E")

col=('#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11','#12','#13','#14','#15','#16','#17','#18','#19')
file=pd.read_csv('Data analysis')
f=ttk.Labelframe(root,text="Data Table")
f.place(x=20,y=100,height=300,width=1450)
tree=ttk.Treeview(f,columns=col,show='headings')
tree.pack(padx=10,pady=10,anchor=CENTER,fill=X)
f2=LabelFrame(root,text="Information",bg="#4C787E",font="Franklin 11 bold")
f2.place(x=30,y=450,height=100,width=250)
l1=Label(f2,text="No Row Selected",bg="#4C787E",font="Franklin 11 bold").place(rely=0.20,relx=0.25)
# tree.bind('<ButtonRelease-1>',item_selected)

scrollx=Scrollbar(f,orient=HORIZONTAL,command=tree.xview)
scrolly=Scrollbar(f,orient=VERTICAL,command=tree.yview)
tree.configure(xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=LEFT,fill=Y)

tree.heading('#1',text='Student Name')
tree.column('#1',width=160)
tree.heading('#2',text='Father\'s Name')
tree.column('#2',width=160)
tree.heading('#3',text='Age')
tree.column('#3',width=60)
tree.heading('#4',text='Address')
tree.heading('#5',text='Mobile Number')
tree.column('#5',width=140)
tree.heading('#6',text='University Id')
tree.column('#6',width=140)
tree.heading('#7',text='Degree')
tree.column('#7',width=100)
tree.heading('#8',text='Branch')
tree.column('#8',width=80)
tree.heading('#9',text='Year')
tree.column('#9',width=80)
tree.heading('#10',text='10th marks')
tree.column('#10',width=80)
tree.heading('#11',text='12th marks')
tree.column('#11',width=80)
tree.heading('#12',text='1st semester')
tree.column('#12',width=80)
tree.heading('#13',text='2nd semester')
tree.column('#13',width=80)
tree.heading('#14',text='3rd semester')
tree.column('#14',width=80)
tree.heading('#15',text='4th semester')
tree.column('#15',width=80)
tree.heading('#16',text='5th semester')
tree.column('#16',width=80)
tree.heading('#17',text='6th semester')
tree.column('#17',width=80)
tree.heading('#18',text='7th semester')
tree.column('#18',width=80)
tree.heading('#19',text='8th semester')
tree.column('#19',width=80)
df=[]
with open('newdata.txt','r') as f:
    for i in f:
        v=i.split(',')
        tree.insert('',END,values=v)


root.mainloop()