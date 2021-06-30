from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter.messagebox as tmsg
import pandas as pd
from tkinter.messagebox import showinfo
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def mypopup(event):
    menu.tk_popup(event.x_root, event.y_root_)
def nextpage():
    root.destroy()
    import update
l=[]
with open('Data.txt','r') as f:

    for i in f:
        i=i.split(',')
        l.append(i)
root =Tk()
root.geometry('1366x768')
root.title('Visulisation')
root.configure(background="Aliceblue")
menu = Menu(root, tearoff=False)
menu.add_command(label="Exit", command=root.quit)
root.bind('<Button-3>', mypopup)

labelframe = LabelFrame(root, text="Student Name", width=200, height=200,bg="light blue", fg="black", font="Castellar 12 bold")
labelframe.place(x=10,y=20,height=60,width=200)
name=l[0][0]
print(name)
Label(labelframe,text=name,font="Arial 15 bold",bg="light blue").pack()

labelframe = LabelFrame(root, text="Father\'s Name",bg="light blue", fg="black", font="Castellar 12 bold")
labelframe.place(x=300,y=20,height=60,width=200)
name=l[0][1]
print(name)
Label(labelframe,text=name,font="Arial 15 bold",bg="light blue").pack()

labelframe = LabelFrame(root, text="AGE",bg="light blue", fg="black", font="Castellar 12 bold")
labelframe.place(x=600,y=20,height=60,width=200)
name=l[0][2]
print(name)
Label(labelframe,text=name,font="Arial 15 bold",bg="light blue").pack()

labelframe = LabelFrame(root, text="University Number",bg="light blue", fg="black", font="Castellar 12 bold")
labelframe.place(x=900,y=20,height=60,width=300)
name=l[0][5]
print(name)
Label(labelframe,text=name,font="Arial 15 bold",bg="light blue").pack()

labelframe = LabelFrame(root, text="Year",bg="light blue", fg="black", font="Castellar 12 bold")
labelframe.place(x=1300,y=20,height=60,width=200)
name=l[0][8]
print(name)
Label(labelframe,text=name,font="Arial 15 bold",bg="light blue").pack()

labelframe = LabelFrame(root, text="Address",bg="light blue", fg="black", font="Castellar 12 bold")
labelframe.place(x=10,y=100,height=60,width=490)
name=l[0][3]
print(name)
Label(labelframe,text=name,font="Arial 15 bold",bg="light blue").pack()

labelframe = LabelFrame(root, text="Mobile Number",bg="light blue", fg="black", font="Castellar 12 bold")
labelframe.place(x=600,y=100,height=60,width=300)
name=l[0][4]
print(name)
Label(labelframe,text=name,font="Arial 15 bold",bg="light blue").pack()

labelframe = LabelFrame(root, text="Course",bg="light blue", fg="black", font="Castellar 12 bold")
labelframe.place(x=1000,y=100,height=60,width=200)
name=l[0][6]
print(name)
Label(labelframe,text=name,font="Arial 15 bold",bg="light blue").pack()

labelframe = LabelFrame(root, text="Branch",bg="light blue", fg="black", font="Castellar 12 bold")
labelframe.place(x=1300,y=100,height=60,width=200)
name=l[0][7]
print(name)
Label(labelframe,text=name,font="Arial 15 bold",bg="light blue").pack()


semmarks=[]
for i in range(11,19):
    semmarks.append(int(l[0][i]))
print(semmarks)
Index=['Sem1','Sem2','Sem3','Sem4','Sem5','Sem6','Sem7','Sem8']
df={"Marks":semmarks,"Semester":Index}
df1=pd.DataFrame(df)
figure1 = plt.Figure(figsize=(6,5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().place(x=800,y=200,height=500,width=700)
df1.plot(kind='line', legend=True, ax=ax1, color='r',marker='o', fontsize=10)
ax1.set_title('Semester marks')

figure2 = Figure(figsize=(4,3), dpi=100)
subplot2 = figure2.add_subplot(111)
labels2 = 'High School', 'Intermideate'
pieSizes = [l[0][9],l[0][10]]
my_colors2 = ['lightblue','lightsteelblue']
explode2 = (0, 0.1)
subplot2.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90)
subplot2.axis('equal')
pie2 = FigureCanvasTkAgg(figure2, root)
pie2.get_tk_widget().place(x=80,y=200,height=500,width=700)

Button(root,text="Previous",command=nextpage).pack()
root.mainloop()
