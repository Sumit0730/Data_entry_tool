import pandas as pd
import numpy as np
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter.messagebox as tmsg
import pandas as pd
from tkinter.messagebox import showinfo
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
# # a = Tk()
# # a.geometry("400x400")
# # labelframe = LabelFrame(a, text="welcome!,c#corner", width=200, cursor="target",
# #                         height=200,bg="yellow", fg="black", font="Castellar")
# # labelframe.pack(side=TOP)
# # a.mainloop()
#
# root=Tk()
#
# l=[1,2,3,4,5,6,7,8]
# Index=['Sem1','Sem2','Sem3','Sem4','Sem5','Sem6','Sem7','Sem8']
#
# # data1={"Semester":l,"Marks":Index}
# # print(data1)
# # df1=pd.DataFrame(data1,columns=['Semester','marks'])
# #
# #
# # figure1 = plt.Figure(figsize=(6,5), dpi=100)
# # ax1 = figure1.add_subplot(111)
# # bar1 = FigureCanvasTkAgg(figure1, root)
# # bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
# # df1.plot(kind='line', legend=True, ax=ax1, color='r',marker='o', fontsize=10)
# # ax1.set_title('Semester marks')
#
# figure2 = Figure(figsize=(4,3), dpi=100)
# subplot2 = figure2.add_subplot(111)
# labels2 = 'High School', 'Intermideate'
# pieSizes = [95,73]
# my_colors2 = ['lightblue','lightsteelblue']
# explode2 = (0, 0.1)
# subplot2.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90)
# subplot2.axis('equal')
# pie2 = FigureCanvasTkAgg(figure2, root)
# pie2.get_tk_widget().pack()
#
#
# root.mainloop()
f=[]
f.append(1)
f.append(2)
f.append(3)
f.append(1)
f.append(8)
f.append(9)
def file():
    with open('Data.txt', 'a') as ff:
        for i in f:
            ff.write(str(i))
            ff.write(",")
        ff.write("\n")
f.append(10)
f.append(10)
f.append(10)
f.append(10)
f.append(10)
f.append(10)
file()


root=Tk()
root.geometry("500x500")
e=Entry(root)
e.place()

root.mainloop()

name=StringVar()
father=StringVar()
age=IntVar()
address=StringVar()
mobile=IntVar()
university=StringVar()
degree=StringVar()
branch=StringVar()
year=IntVar()
mark10=IntVar()
mark12=IntVar()
sem1=IntVar()
sem2=IntVar()
sem3=IntVar()
sem4=IntVar()
sem5=IntVar()
sem6=IntVar()
sem7=IntVar()
sem8=IntVar()



Entry(f2,textvariable=father).place(x=180,y=33,height=15)
Entry(f2,textvariable=age).place(x=180,y=53,height=15)
Entry(f2,textvariable=address).place(x=180,y=73,height=15)
Entry(f2,textvariable=mobile).place(x=180,y=93,height=15)
Entry(f2,textvariable=university).place(x=180,y=113,height=15)
Entry(f2,textvariable=degree).place(x=180,y=133,height=15)
Entry(f2,textvariable=branch).place(x=180,y=153,height=15)
Entry(f2,textvariable=year).place(x=180,y=173,height=15)
Entry(f2,textvariable=mark10).place(x=180,y=193,height=15)
Entry(f2,textvariable=mark12).place(x=900,y=13,height=15)
Entry(f2,textvariable=sem1).place(x=900,y=33,height=15)
Entry(f2,textvariable=sem2).place(x=900,y=53,height=15)
Entry(f2,textvariable=sem3).place(x=900,y=73,height=15)
Entry(f2,textvariable=sem4).place(x=900,y=93,height=15)
Entry(f2,textvariable=sem5).place(x=900,y=113,height=15)
Entry(f2,textvariable=sem6).place(x=900,y=133,height=15)
Entry(f2,textvariable=sem7).place(x=900,y=153,height=15)
Entry(f2,textvariable=sem8).place(x=900,y=173,height=15)





def displayfunction():

    root = Tk()
    # root.maxsize(1000, 900)
    root.minsize(1500, 1600)
    root.geometry("1366x768")
    root.title("Data Visualization")
    root.configure(background="#4C787E")
    style=ttk.Style()
    style.theme_use('default')
    style.configure("Treeview",background='sky blue')
    style.map('Treeview',background=[('selected','green')])

    def clear():
        with open('Data.txt', 'w') as f:
            f.truncate(0)

    def view():
        root.destroy()
        rowfunction()
        # import Rowdata
        clear()

    def item_selected(event):
        rowvalue = []
        curritem = tree.focus()
        l1 = Label(f2, text=f"{curritem} item selected ", font="Franklin 11 bold", bg="#4C787E").place(rely=0.20,
                                                                                                       relx=0.25)
        rowvalue = tree.item(curritem)['values']
        with open('Data.txt', 'a') as f:
            for i in rowvalue:
                f.write(f"{i},")

    def check():
        val = item_selected(event='<ButtonRelease-1>')

        val = tmsg.showinfo("Information", "Row selected")
        if val == "ok":
            view()
        else:
            tmsg.showerror("Invalid", "No field selected")

    Frame(root, bg="#348781", borderwidth=30, relief=SUNKEN).pack(side=LEFT, fill=Y, anchor=W)
    Frame(root, bg="#348781", borderwidth=30, relief=SUNKEN).pack(side=RIGHT, fill=Y, anchor=E)
    Frame(root, bg="#348781", borderwidth=30, relief=SUNKEN).pack(side=BOTTOM, fill=X, anchor=S)
    f1 = Frame(root, bg="#348781", borderwidth=6, relief=SUNKEN)
    f1.pack(side=TOP, fill=X, anchor=W)
    Label(f1, text="Data Table View", fg="black", bg="#348781", font=" Franklin 15 bold", pady=5).pack(pady=5, anchor=W)

    col = (
    '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11', '#12', '#13', '#14', '#15', '#16', '#17', '#18',
    '#19')
    file = pd.read_csv('Data analysis')
    f = ttk.Labelframe(root, text="Data Table")
    f.place(x=20, y=100, height=300, width=1450)
    tree = ttk.Treeview(f, columns=col, show='headings')
    tree.pack(padx=10, pady=10, anchor=CENTER, fill=X)
    f2 = LabelFrame(root, text="Information", bg="#4C787E", font="Franklin 11 bold")
    f2.place(x=30, y=450, height=100, width=250)
    l1 = Label(f2, text="No Row Selected", bg="#4C787E", font="Franklin 11 bold").place(rely=0.20, relx=0.25)
    tree.bind('<ButtonRelease-1>', item_selected)
    tree.tag_configure('oddrow',background='white')
    tree.tag_configure('evenrow',background='sky blue')

    scrollx = Scrollbar(f, orient=HORIZONTAL, command=tree.xview)
    scrolly = Scrollbar(f, orient=VERTICAL, command=tree.yview)
    tree.configure(xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
    scrollx.pack(side=BOTTOM, fill=X)
    scrolly.pack(side=LEFT, fill=Y)

    tree.heading('#1', text='Student Name')
    tree.column('#1', width=160)
    tree.heading('#2', text='Father\'s Name')
    tree.column('#2', width=160)
    tree.heading('#3', text='Age')
    tree.column('#3', width=60)
    tree.heading('#4', text='Address')
    tree.heading('#5', text='Mobile Number')
    tree.column('#5', width=140)
    tree.heading('#6', text='University Id')
    tree.column('#6', width=140)
    tree.heading('#7', text='Degree')
    tree.column('#7', width=100)
    tree.heading('#8', text='Branch')
    tree.column('#8', width=80)
    tree.heading('#9', text='Year')
    tree.column('#9', width=80)
    tree.heading('#10', text='10th marks')
    tree.column('#10', width=80)
    tree.heading('#11', text='12th marks')
    tree.column('#11', width=80)
    tree.heading('#12', text='1st semester')
    tree.column('#12', width=80)
    tree.heading('#13', text='2nd semester')
    tree.column('#13', width=80)
    tree.heading('#14', text='3rd semester')
    tree.column('#14', width=80)
    tree.heading('#15', text='4th semester')
    tree.column('#15', width=80)
    tree.heading('#16', text='5th semester')
    tree.column('#16', width=80)
    tree.heading('#17', text='6th semester')
    tree.column('#17', width=80)
    tree.heading('#18', text='7th semester')
    tree.column('#18', width=80)
    tree.heading('#19', text='8th semester')
    tree.column('#19', width=80)
    df = []
    with open('newdata.txt', 'r') as f:
        cout=0
        for i in f:
            if cout%2==0:
                v = i.split(',')
                tree.insert('', END, values=v,tag=('evenrow',))
            else:
                v = i.split(',')
                tree.insert('', END, values=v,tag=('oddrow',))
            cout+=1
    # def nextpage():
    #     import Entrypage
    #     # tree.insert('',END,values=(Entrypage.namevalue.get(),))
    Button(f2, text="View", bg="#4C787E", command=check, font="Franklin 11 bold").place(rely=0.65, relx=0.35, height=20, width=50)
    # Button(f2,text="Add",command=nextpage).place(rely=0.65,relx=0.49,height=20,width=50)



    root.mainloop()


if combobox.get() == "1st Semester":
    sem1 = Entry(root, bg="light sky blue", width=30)
    sem1.place(x=1000, y=200)
    Label(root, text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=200)

elif combobox.get() == "2nd Semester":
    sem1 = Entry(root, bg="light sky blue", width=30)
    sem1.place(x=1000, y=200)
    Label(root, text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=200)

    sem2 = Entry(root, textvariable=sem2, bg="light sky blue", width=30)
    sem2.place(x=1000, y=240)
    Label(root, text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=240)
elif combobox.get() == "3rd Semester":
    sem1 = Entry(root, bg="light sky blue", width=30)
    sem1.place(x=1000, y=200)
    Label(root, text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=200)

    sem2 = Entry(root, textvariable=sem2, bg="light sky blue", width=30)
    sem2.place(x=1000, y=240)
    Label(root, text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=240)

    sem3 = Entry(root, textvariable=sem3, bg="light sky blue", width=30)
    sem3.place(x=1000, y=280)
    Label(root, text="3rd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=280)

elif combobox.get() == "4th Semester":
    sem1 = Entry(root, bg="light sky blue", width=30)
    sem1.place(x=1000, y=200)
    Label(root, text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=200)

    sem2 = Entry(root, textvariable=sem2, bg="light sky blue", width=30)
    sem2.place(x=1000, y=240)
    Label(root, text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=240)

    sem3 = Entry(root, textvariable=sem3, bg="light sky blue", width=30)
    sem3.place(x=1000, y=280)
    Label(root, text="3rd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=280)

    sem4 = Entry(root, textvariable=sem4, bg="light sky blue", width=30)
    sem4.place(x=1000, y=320)
    Label(root, text="4th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=320)
elif combobox.get() == "5th Semester":
    sem1 = Entry(root, bg="light sky blue", width=30)
    sem1.place(x=1000, y=200)
    Label(root, text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=200)

    sem2 = Entry(root, textvariable=sem2, bg="light sky blue", width=30)
    sem2.place(x=1000, y=240)
    Label(root, text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=240)

    sem3 = Entry(root, textvariable=sem3, bg="light sky blue", width=30)
    sem3.place(x=1000, y=280)
    Label(root, text="3rd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=280)

    sem4 = Entry(root, textvariable=sem4, bg="light sky blue", width=30)
    sem4.place(x=1000, y=320)
    Label(root, text="4th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=320)

    sem5 = Entry(root, textvariable=sem5, bg="light sky blue", width=30)
    sem5.place(x=1000, y=360)
    Label(root, text="5th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=360)
elif combobox.get() == "6th Semester":
    sem1 = Entry(root, bg="light sky blue", width=30)
    sem1.place(x=1000, y=200)
    Label(root, text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=200)

    sem2 = Entry(root, textvariable=sem2, bg="light sky blue", width=30)
    sem2.place(x=1000, y=240)
    Label(root, text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=240)

    sem3 = Entry(root, textvariable=sem3, bg="light sky blue", width=30)
    sem3.place(x=1000, y=280)
    Label(root, text="3rd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=280)

    sem4 = Entry(root, textvariable=sem4, bg="light sky blue", width=30)
    sem4.place(x=1000, y=320)
    Label(root, text="4th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=320)

    sem5 = Entry(root, textvariable=sem5, bg="light sky blue", width=30)
    sem5.place(x=1000, y=360)
    Label(root, text="5th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=360)

    sem6 = Entry(root, textvariable=sem6, bg="light sky blue", width=30)
    sem6.place(x=1000, y=400)
    Label(root, text="6th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=400)
elif combobox.get() == "7th Semester":
    sem1 = Entry(root, bg="light sky blue", width=30)
    sem1.place(x=1000, y=200)
    Label(root, text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=200)

    sem2 = Entry(root, textvariable=sem2, bg="light sky blue", width=30)
    sem2.place(x=1000, y=240)
    Label(root, text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=240)

    sem3 = Entry(root, textvariable=sem3, bg="light sky blue", width=30)
    sem3.place(x=1000, y=280)
    Label(root, text="3rd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=280)

    sem4 = Entry(root, textvariable=sem4, bg="light sky blue", width=30)
    sem4.place(x=1000, y=320)
    Label(root, text="4th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=320)

    sem5 = Entry(root, textvariable=sem5, bg="light sky blue", width=30)
    sem5.place(x=1000, y=360)
    Label(root, text="5th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=360)

    sem6 = Entry(root, textvariable=sem6, bg="light sky blue", width=30)
    sem6.place(x=1000, y=400)
    Label(root, text="6th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=400)

    sem7 = Entry(root, textvariable=sem7, bg="light sky blue", width=30)
    sem7.place(x=1000, y=440)
    Label(root, text="7th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=440)
elif combobox.get() == "8th Semester":
    sem1 = Entry(root, bg="light sky blue", width=30)
    sem1.place(x=1000, y=200)
    Label(root, text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=200)

    sem2 = Entry(root, textvariable=sem2, bg="light sky blue", width=30)
    sem2.place(x=1000, y=240)
    Label(root, text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=240)

    sem3 = Entry(root, textvariable=sem3, bg="light sky blue", width=30)
    sem3.place(x=1000, y=280)
    Label(root, text="3rd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=280)

    sem4 = Entry(root, textvariable=sem4, bg="light sky blue", width=30)
    sem4.place(x=1000, y=320)
    Label(root, text="4th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=320)

    sem5 = Entry(root, textvariable=sem5, bg="light sky blue", width=30)
    sem5.place(x=1000, y=360)
    Label(root, text="5th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=360)

    sem6 = Entry(root, textvariable=sem6, bg="light sky blue", width=30)
    sem6.place(x=1000, y=400)
    Label(root, text="6th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=400)

    sem7 = Entry(root, textvariable=sem7, bg="light sky blue", width=30)
    sem7.place(x=1000, y=440)
    Label(root, text="7th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=440)

    sem8 = Entry(root, textvariable=sem8, bg="light sky blue", width=30)
    sem8.place(x=1000, y=480)
    Label(root, text="8th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
        x=700, y=480)




c.execute("INSERT INTO customers VALUES (:Sname, :fathername, :age, :address, :mobile, :Id, :degree,:branch,:year,:mark10,:mark12,:sem1,:sem2,:sem3,:sem4,:sem5,:sem6,:sem7,:sem8)",
                          { 'Sname':record[0],'fathername':record[1],'age':record[2],'address':record[3],'mobile':record[4],'Id':record[5]
                            ,'degree':record[6],'branch':record[7],'year':record[8],'mark10':record[9],'mark12':record[10],'sem1':record[11],
                            'sem2': record[12],'sem3':record[13],'sem4':record[14],'sem5':record[15],'sem6':record[16],'sem7':record[17],'sem8':record[18]
                          }
                          )
,'sem2': record[12], 'sem3': record[13], 'sem4': record[14], 'sem5': record[15], 'sem6': record[16],'sem7': record[17], 'sem8': record[18]