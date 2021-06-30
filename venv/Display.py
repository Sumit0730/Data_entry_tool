from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter.messagebox as tmsg
import pandas as pd
from tkinter.messagebox import showinfo
import fileinput
import sys

root = Tk()
# root.maxsize(1000, 900)
root.minsize(1500,1600)
root.geometry("1366x768")
root.title("Data Visualization")
root.configure(background="#4C787E")
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background='sky blue')
style.map('Treeview', background=[('selected', 'green')])

def clear():
    with open('Data.txt','w') as f:
        f.truncate(0)
def view():
    root.destroy()
    import Rowdata
    clear()
def item_selected(event):
    rowvalue = []
    curritem=tree.focus()
    l1 = Label(f2, text=f"{curritem} item selected ",font="Franklin 11 bold",bg="#4C787E").place(rely=0.20,relx=0.25)
    rowvalue=tree.item(curritem)['values']
    with open('Data.txt','a') as f:
        for i in rowvalue:
            f.write(f"{i},")

    # val=tmsg.showinfo("Information","Row selected")
    # return val
def check():
    val=item_selected(event='<ButtonRelease-1>')

    val = tmsg.showinfo("Information", "Row selected")
    if val=="ok":
        view()
    else:
        tmsg.showerror("Invalid","No field selected")
def selectrecord():
    item=tree.focus()
    value=tree.item(item,"values")
    names.delete(0,END)
    father.delete(0,END)
    age.delete(0,END)
    address.delete(0,END)
    mobile.delete(0,END)
    Id.delete(0,END)
    degree.delete(0,END)
    branch.delete(0,END)
    year.delete(0,END)
    mark10.delete(0,END)
    mark12.delete(0,END)
    sem1.delete(0,END)
    sem2.delete(0,END)
    sem3.delete(0,END)
    sem4.delete(0,END)
    sem5.delete(0,END)
    sem6.delete(0,END)
    sem7.delete(0,END)
    sem8.delete(0,END)
    names.insert(0,value[0])
    father.insert(0,value[1])
    age.insert(0,value[2])
    address.insert(0,value[3])
    mobile.insert(0,value[4])
    Id.insert(0,value[5])
    degree.insert(0,value[6])
    branch.insert(0,value[7])
    year.insert(0,value[8])
    mark10.insert(0,value[9])
    mark12.insert(0,value[10])
    sem1.insert(0,value[11])
    sem2.insert(0,value[12])
    sem3.insert(0,value[13])
    sem4.insert(0,value[14])
    sem5.insert(0,value[15])
    sem6.insert(0,value[16])
    sem7.insert(0,value[17])
    sem8.insert(0,value[18])
def Updaterecord():
    names.delete(0,END)
def deleterecord():
    pass

Frame(root, bg="#348781", borderwidth=30, relief=SUNKEN).pack(side=LEFT, fill=Y, anchor=W)
Frame(root, bg="#348781", borderwidth=30, relief=SUNKEN).pack(side=RIGHT, fill=Y, anchor=E)
Frame(root, bg="#348781", borderwidth=30, relief=SUNKEN).pack(side=BOTTOM, fill=X, anchor=S)
f1 = Frame(root, bg="#348781", borderwidth=6, relief=SUNKEN)
f1.pack(side=TOP, fill=X, anchor=W)
Label(f1, text="Data Table View", fg="black", bg="#348781", font=" Franklin 15 bold", pady=5).pack(pady=5,anchor=W)

col=('#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11','#12','#13','#14','#15','#16','#17','#18','#19')
file=pd.read_csv('Data analysis')
f=ttk.Labelframe(root,text="Data Table")
f.place(x=20,y=80,height=300,width=1470)
tree=ttk.Treeview(f,columns=col,show='headings')
tree.pack(padx=20,pady=10,anchor=CENTER,fill=X)
# f2=LabelFrame(root,text="Information",bg="#4C787E",font="Franklin 11 bold")
# f2.place(x=30,y=450,height=100,width=250)
# l1=Label(f2,text="No Row Selected",bg="#4C787E",font="Franklin 11 bold").place(rely=0.20,relx=0.25)
# tree.bind('<ButtonRelease-1>',item_selected)
tree.tag_configure('oddrow', background='white')
tree.tag_configure('evenrow', background='sky blue')

scrollx=Scrollbar(f,orient=HORIZONTAL,command=tree.xview)
scrolly=Scrollbar(f,orient=VERTICAL,command=tree.yview)
tree.configure(xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y,anchor=N)

# headings
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
df = []
with open('newdata.txt', 'r') as f:
    cout = 0
    for i in f:
        if cout % 2 == 0:
            v = i.split(',')
            tree.insert('', END, values=v, tag=('evenrow',))
        else:
            v = i.split(',')
            tree.insert('', END, values=v, tag=('oddrow',))
        cout += 1

f2=LabelFrame(root,text="Record",relief=RIDGE)
f2.place(x=20,y=400,height=250,width=1470)

# labels
Label(f2,text="Name",fg="black",font=" Franklin 9 bold",pady=5).place(x=20,y=10)
Label(f2,text="Father\'s Name",fg="black",font=" Franklin 9 bold",pady=5).place(x=20,y=30)
Label(f2,text="Age",fg="black",font=" Franklin 9 bold",pady=5).place(x=20,y=50)
Label(f2,text="Address",fg="black",font=" Franklin 9 bold",pady=5).place(x=20,y=70)
Label(f2,text="Mobile number",fg="black",font=" Franklin 9 bold",pady=5).place(x=20,y=90)
Label(f2,text="University Id",fg="black",font=" Franklin 9 bold",pady=5).place(x=20,y=110)
Label(f2,text="Degree",fg="black",font=" Franklin 9 bold",pady=5).place(x=20,y=130)
Label(f2,text="Branch",fg="black",font=" Franklin 9 bold",pady=5).place(x=20,y=150)
Label(f2,text="Year",fg="black",font=" Franklin 9 bold",pady=5).place(x=20,y=170)
Label(f2,text="10th marks",fg="black",font=" Franklin 9 bold",pady=5).place(x=20,y=190)

Label(f2,text="12th marks",fg="black",font=" Franklin 9 bold",pady=5).place(x=700,y=10)
Label(f2,text="1st semester",fg="black",font=" Franklin 9 bold",pady=5).place(x=700,y=30)
Label(f2,text="2nd semester",fg="black",font=" Franklin 9 bold",pady=5).place(x=700,y=50)
Label(f2,text="3rd semester",fg="black",font=" Franklin 9 bold",pady=5).place(x=700,y=70)
Label(f2,text="4th semester",fg="black",font=" Franklin 9 bold",pady=5).place(x=700,y=90)
Label(f2,text="5th semester",fg="black",font=" Franklin 9 bold",pady=5).place(x=700,y=110)
Label(f2,text="6th semester",fg="black",font=" Franklin 9 bold",pady=5).place(x=700,y=130)
Label(f2,text="7th semester",fg="black",font=" Franklin 9 bold",pady=5).place(x=700,y=150)
Label(f2,text="8th semester",fg="black",font=" Franklin 9 bold",pady=5).place(x=700,y=170)

# entry boxes
names=Entry(f2)
names.place(x=180,y=13,height=15)
father=Entry(f2)
father.place(x=180,y=33,height=15)
age=Entry(f2)
age.place(x=180,y=53,height=15)
address=Entry(f2)
address.place(x=180,y=73,height=15)
mobile=Entry(f2)
mobile.place(x=180,y=93,height=15)
Id=Entry(f2)
Id.place(x=180,y=113,height=15)
degree=Entry(f2)
degree.place(x=180,y=133,height=15)
branch=Entry(f2)
branch.place(x=180,y=153,height=15)
year=Entry(f2)
year.place(x=180,y=173,height=15)
mark10=Entry(f2)
mark10.place(x=180,y=193,height=15)
mark12=Entry(f2)
mark12.place(x=900,y=13,height=15)
sem1=Entry(f2)
sem1.place(x=900,y=33,height=15)
sem2=Entry(f2)
sem2.place(x=900,y=53,height=15)
sem3=Entry(f2)
sem3.place(x=900,y=73,height=15)
sem4=Entry(f2)
sem4.place(x=900,y=93,height=15)
sem5=Entry(f2)
sem5.place(x=900,y=113,height=15)
sem6=Entry(f2)
sem6.place(x=900,y=133,height=15)
sem7=Entry(f2)
sem7.place(x=900,y=153,height=15)
sem8=Entry(f2)
sem8.place(x=900,y=173,height=15)

# Buttons
f3=LabelFrame(root,text="Commands")
f3.place(x=20,y=670,height=80,width=1470)
Button(f3,text="Select Record",command=selectrecord).place(x=10,y=10)
Button(f3,text="Update Record",command=Updaterecord).place(x=120,y=10)
Button(f3,text="Delete Record",command=deleterecord).place(x=230,y=10)
Button(f3,text="View Record",command=view).place(x=340,y=10)

def up():
	rows = tree.selection()
	for row in rows:
		tree.move(row,tree.parent(row),tree.index(row)-1)
Button(f3,text="Move up",command=up).place(x=450,y=10)

def down():
	rows =tree.selection()
	for row in reversed(rows):
		tree.move(row, tree.parent(row), tree.index(row)+1)
Button(f3,text="Move Down",command=down).place(x=550,y=10)

def remove_one():
	x = tree.selection()[0]
	tree.delete(x)
Button(f3,text="Remove",command=remove_one).place(x=660,y=10)

root.mainloop()