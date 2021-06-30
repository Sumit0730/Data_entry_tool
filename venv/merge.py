from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tmsg
from tkinter import ttk
import pandas as pd
from tkinter.messagebox import showinfo
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import sqlite3

def sign():
    def nextPage():
        root.destroy()
        updatefunction()
        # import update

    global value
    def getvalue():

        print(uservalue.get())
        print(passvalue.get())
        if uservalue.get() != "admin":
            tmsg.showerror("Error", "Invalid username")
        elif passvalue.get() != "admin":
            tmsg.showerror("Error", "Invalid password")
        else:
            value=tmsg.showinfo("Login Successfully", "Press OK to continue")
            print(value)
            if value == "ok":
                nextPage()
                # bt = Button(text="Next", command=nextPage, bg="#7CFC00", font="Franklin 12 bold").place(x=800, y=600)

    root = Tk()

    root.geometry("700x600")
    root.minsize(400,400)
    f1 = Frame(root, bg="#58D68D", borderwidth=4, relief=SUNKEN)
    f1.pack(side=TOP, fill=X, anchor=W)
    l = Label(f1, text="Data Analysis and Visualization", fg="#34495E", bg="#58D68D", font=" Franklin 15 bold",pady=5)
    l.pack()

    f2 = Frame(root, bg="#58D68D", borderwidth=16, relief=SUNKEN)
    f2.pack(side=BOTTOM, fill=X, anchor=S)
    Frame(root, bg="#58D68D", borderwidth=6, relief=SUNKEN).pack(side=LEFT, fill=X, anchor=W)

    root.title("Data Visualization")
    root.configure(background="#27AE60")

    can=Canvas(root,height=400,width=450,bg="#27AE60")
    can.place(x=140,y=120)

    im = Image.open("locksmith.png")
    im = im.resize((30,30), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(im)
    can.create_image(130,200,image=img)

    im = Image.open("lock.png")
    im = im.resize((30,30), Image.ANTIALIAS)
    imgi = ImageTk.PhotoImage(im)
    can.create_image(130,250,image=imgi)

    # t=Label(text="Username",bg="#27AE60",fg="green",font=" Franklin 20 bold",pady=10).place(x=120,y=300)
    # t=Label(text="Password",bg="#27AE60",fg="green",font=" Franklin 20 bold",pady=12).place(x=120,y=350)
    uservalue=StringVar()
    passvalue=StringVar()
    userentry=Entry(textvariable=uservalue,bg="light green",width=25)
    passentry=Entry(textvariable=passvalue,bg="light green",width=25)
    userentry.place(x=300,y=310)
    passentry.place(x=300,y=360)
    b=Button(text="Login", command=getvalue,bg="#27AE60",fg="#4A235A",font="Franklin 12 bold").place(x=340,y=430)
    f2=Frame(root, bg="#27AE60", borderwidth=25, relief=SUNKEN)
    f2.pack(side=LEFT, fill=Y, anchor=W)
    f3 = Frame(root, bg="#27AE60", borderwidth=25, relief=SUNKEN)
    f3.pack(side=RIGHT, fill=Y, anchor=E)
    # ckvalue=IntVar()
    # ck=Checkbutton(text=" I am not a Robot",variable=ckvalue,font="Franklin 12 bold",bg="#27AE60").place(x=600,y=530)
    im=Image.open("login.png")
    im=im.resize((120,120), Image.ANTIALIAS)
    ph=ImageTk.PhotoImage(im)
    l=Label(image=ph,bg="#27AE60")
    l.place(x=300,y=150)


    root.mainloop()

def datafunction():


    def dataframe(event='<<ComboboxSelected>>'):
        val = tmsg.showinfo("Successful", "Data Uploaded successfully")
        l = []
        l.append(name.get())
        l.append(father.get())
        l.append(age.get())
        l.append(address.get())
        l.append(mobile.get())
        l.append(Id.get())
        l.append(degree.get())
        l.append(branch.get())
        l.append(year.get())
        l.append(mark10.get())
        l.append(mark12.get())
        if combobox.get() == "1st Semester":
            l.append(sem1.get())
        elif combobox.get() == "2nd Semester":
            l.append(sem1.get())
            l.append(sem2.get())
        elif combobox.get() == "3rd Semester":
            l.append(sem1.get())
            l.append(sem2.get())
            l.append(sem3.get())
        elif combobox.get() == "4th Semester":
            l.append(sem1.get())
            l.append(sem2.get())
            l.append(sem3.get())
            l.append(sem4.get())
        elif combobox.get() == "5th Semester":
            l.append(sem1.get())
            l.append(sem2.get())
            l.append(sem3.get())
            l.append(sem4.get())
            l.append(sem5.get())
        elif combobox.get() == "6th Semester":
            l.append(sem1.get())
            l.append(sem2.get())
            l.append(sem3.get())
            l.append(sem4.get())
            l.append(sem5.get())
            l.append(sem6.get())
        elif combobox.get() == "7th Semester":
            l.append(sem1.get())
            l.append(sem2.get())
            l.append(sem3.get())
            l.append(sem4.get())
            l.append(sem5.get())
            l.append(sem6.get())
            l.append(sem7.get())
        elif combobox.get() == "8th Semester":
            l.append(sem1.get())
            l.append(sem2.get())
            l.append(sem3.get())
            l.append(sem4.get())
            l.append(sem5.get())
            l.append(sem6.get())
            l.append(sem7.get())
            l.append(sem8.get())
        conn = sqlite3.connect('datavisual.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE if not exists datavalue (Sname text,fathername text,age INTEGER ,address text,mobile Integer
        ,Id Integer ,degree text,branch text,year INTEGER ,mark10 INTEGER ,mark12 INTEGER ,sem1 integer ,sem2 integer ,sem3 integer ,sem4 integer ,
        sem5 integer ,sem6 integer ,sem7 integer ,sem8 integer)""")
        record=l
        if combobox.get()=="1st Semester":
            c.execute("INSERT INTO datavalue VALUES (:Sname, :fathername, :age, :address, :mobile, :Id, :degree,:branch,:year,:mark10,:mark12,:sem1,:sem2,:sem3,:sem4,:sem5,:sem6,:sem7,:sem8)",
                {'Sname': record[0], 'fathername': record[1], 'age': record[2], 'address': record[3], 'mobile': record[4],
                 'Id': record[5], 'degree': record[6], 'branch': record[7], 'year': record[8], 'mark10': record[9], 'mark12': record[10],
                 'sem1': record[11]
                 })
        elif combobox.get()=="2nd Semester":
            c.execute(
                "INSERT INTO datavalue VALUES (:Sname, :fathername, :age, :address, :mobile, :Id, :degree,:branch,:year,:mark10,:mark12,:sem1,:sem2,:sem3,:sem4,:sem5,:sem6,:sem7,:sem8)",
                {'Sname': record[0], 'fathername': record[1], 'age': record[2], 'address': record[3],
                 'mobile': record[4],'Id': record[5], 'degree': record[6], 'branch': record[7], 'year': record[8], 'mark10': record[9],'mark12': record[10],
                 'sem1': record[11],'sem2': record[12]
                 })
        elif combobox.get() == "3rd Semester":
            c.execute(
                "INSERT INTO datavalue VALUES (:Sname, :fathername, :age, :address, :mobile, :Id, :degree,:branch,:year,:mark10,:mark12,:sem1,:sem2,:sem3,:sem4,:sem5,:sem6,:sem7,:sem8)",
                {'Sname': record[0], 'fathername': record[1], 'age': record[2], 'address': record[3],'mobile': record[4], 'Id': record[5], 'degree': record[6], 'branch': record[7], 'year': record[8],
                 'mark10': record[9], 'mark12': record[10],'sem1': record[11], 'sem2': record[12], 'sem3': record[13]
                 })
        elif combobox.get() == "4th Semester":
            c.execute(
                "INSERT INTO datavalue VALUES (:Sname, :fathername, :age, :address, :mobile, :Id, :degree,:branch,:year,:mark10,:mark12,:sem1,:sem2,:sem3,:sem4,:sem5,:sem6,:sem7,:sem8)",
                {'Sname': record[0], 'fathername': record[1], 'age': record[2], 'address': record[3],
                 'mobile': record[4], 'Id': record[5], 'degree': record[6], 'branch': record[7], 'year': record[8],
                 'mark10': record[9], 'mark12': record[10], 'sem1': record[11], 'sem2': record[12], 'sem3': record[13], 'sem4': record[14]
                 })
        elif combobox.get() == "5th Semester":
            c.execute(
                "INSERT INTO datavalue VALUES (:Sname, :fathername, :age, :address, :mobile, :Id, :degree,:branch,:year,:mark10,:mark12,:sem1,:sem2,:sem3,:sem4,:sem5,:sem6,:sem7,:sem8)",
                {'Sname': record[0], 'fathername': record[1], 'age': record[2], 'address': record[3],
                 'mobile': record[4], 'Id': record[5], 'degree': record[6], 'branch': record[7], 'year': record[8],
                 'mark10': record[9], 'mark12': record[10], 'sem1': record[11], 'sem2': record[12], 'sem3': record[13], 'sem4': record[14], 'sem5': record[15]
                 })
        elif combobox.get() == "6th Semester":
            c.execute(
                "INSERT INTO datavalue VALUES (:Sname, :fathername, :age, :address, :mobile, :Id, :degree,:branch,:year,:mark10,:mark12,:sem1,:sem2,:sem3,:sem4,:sem5,:sem6,:sem7,:sem8)",
                {'Sname': record[0], 'fathername': record[1], 'age': record[2], 'address': record[3],
                 'mobile': record[4], 'Id': record[5], 'degree': record[6], 'branch': record[7], 'year': record[8],
                 'mark10': record[9], 'mark12': record[10], 'sem1': record[11], 'sem2': record[12], 'sem3': record[13], 'sem4': record[14], 'sem5': record[15], 'sem6': record[16]
                 })
        elif combobox.get() == "7th Semester":
            c.execute(
                "INSERT INTO datavalue VALUES (:Sname, :fathername, :age, :address, :mobile, :Id, :degree,:branch,:year,:mark10,:mark12,:sem1,:sem2,:sem3,:sem4,:sem5,:sem6,:sem7,:sem8)",
                {'Sname': record[0], 'fathername': record[1], 'age': record[2], 'address': record[3],
                 'mobile': record[4], 'Id': record[5], 'degree': record[6], 'branch': record[7], 'year': record[8],
                 'mark10': record[9], 'mark12': record[10], 'sem1': record[11], 'sem2': record[12], 'sem3': record[13], 'sem4': record[14], 'sem5': record[15], 'sem6': record[16],'sem7': record[17]
                 })
        elif combobox.get() == "8th Semester":
            c.execute(
                "INSERT INTO datavalue VALUES (:Sname, :fathername, :age, :address, :mobile, :Id, :degree,:branch,:year,:mark10,:mark12,:sem1,:sem2,:sem3,:sem4,:sem5,:sem6,:sem7,:sem8)",
                {'Sname': record[0], 'fathername': record[1], 'age': record[2], 'address': record[3],'mobile': record[4], 'Id': record[5], 'degree': record[6], 'branch': record[7], 'year': record[8],
                 'mark10': record[9], 'mark12': record[10], 'sem1': record[11], 'sem2': record[12], 'sem3': record[13], 'sem4': record[14], 'sem5': record[15], 'sem6': record[16],'sem7': record[17], 'sem8': record[18]
                 })
        conn.commit()
        conn.close()
        close()
        updatefunction()

    def Clearvalue():
        name.delete(0,END)
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
        sem1.set("")
        sem2.set("")
        sem3.set("")
        sem4.set("")
        sem5.set("")
        sem6.set("")
        sem7.set("")
        sem8.set("")

    def semesterbox(event):
        if combobox.get() == "1st Semester":
            sem11=Entry(root, textvariable=sem1, bg="light sky blue", width=30)
            sem11.place(x=1000, y=200)
            Label(root, text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=200)
        elif combobox.get() == "2nd Semester":
            sem11=Entry(root, textvariable=sem1, bg="light sky blue", width=30)
            sem11.place(x=1000, y=200)
            Label(root, text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=200)

            sem12=Entry(root, textvariable=sem2, bg="light sky blue", width=30)
            sem12.place(x=1000, y=240)
            Label(root, text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=240)
        elif combobox.get() == "3rd Semester":
            sem11=Entry(root, textvariable=sem1, bg="light sky blue", width=30)
            sem11.place(x=1000, y=200)
            Label(root, text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=200)

            sem12=Entry(root, textvariable=sem2, bg="light sky blue", width=30)
            sem12.place(x=1000, y=240)
            Label(root, text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=240)

            sem13=Entry(root, textvariable=sem3, bg="light sky blue", width=30)
            sem13.place(x=1000, y=280)
            Label(root, text="3rd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=280)
        elif combobox.get() == "4th Semester":
            sem11=Entry(root, textvariable=sem1, bg="light sky blue", width=30)
            sem11.place(x=1000, y=200)
            Label(root, text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=200)

            sem12=Entry(root, textvariable=sem2, bg="light sky blue", width=30)
            sem12.place(x=1000, y=240)
            Label(root, text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=240)

            sem13=Entry(root, textvariable=sem3, bg="light sky blue", width=30)
            sem13.place(x=1000, y=280)
            Label(root, text="3rd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=280)

            sem14=Entry(root, textvariable=sem4, bg="light sky blue", width=30)
            sem14.place(x=1000, y=320)
            Label(root, text="4th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=320)
        elif combobox.get() == "5th Semester":
            sem11=Entry(root, textvariable=sem1, bg="light sky blue", width=30)
            sem11.place(x=1000, y=200)
            Label(root, text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=200)

            sem12=Entry(root, textvariable=sem2, bg="light sky blue", width=30)
            sem12.place(x=1000, y=240)
            Label(root, text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=240)

            sem13=Entry(root, textvariable=sem3, bg="light sky blue", width=30)
            sem13.place(x=1000, y=280)
            Label(root, text="3rd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=280)

            sem14=Entry(root, textvariable=sem4, bg="light sky blue", width=30)
            sem14.place(x=1000, y=320)
            Label(root, text="4th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=320)

            sem15=Entry(root, textvariable=sem5, bg="light sky blue", width=30)
            sem15.place(x=1000, y=360)
            Label(root, text="5th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=360)

        elif combobox.get() == "6th Semester":
            sem11=Entry(root, textvariable=sem1, bg="light sky blue", width=30)
            sem11.place(x=1000, y=200)
            Label(root, text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=200)

            sem12=Entry(root, textvariable=sem2, bg="light sky blue", width=30)
            sem12.place(x=1000, y=240)
            Label(root, text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=240)

            sem13=Entry(root, textvariable=sem3, bg="light sky blue", width=30)
            sem13.place(x=1000, y=280)
            Label(root, text="3rd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=280)

            sem14=Entry(root, textvariable=sem4, bg="light sky blue", width=30)
            sem14.place(x=1000, y=320)
            Label(root, text="4th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=320)

            sem15=Entry(root, textvariable=sem5, bg="light sky blue", width=30)
            sem15.place(x=1000, y=360)
            Label(root, text="5th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=360)

            sem16=Entry(root, textvariable=sem6, bg="light sky blue", width=30)
            sem16.place(x=1000, y=400)
            Label(root, text="6th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=400)
        elif combobox.get() == "7th Semester":
            sem11=Entry(root, textvariable=sem1, bg="light sky blue", width=30)
            sem11.place(x=1000, y=200)
            Label(root, text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=200)

            sem12=Entry(root, textvariable=sem2, bg="light sky blue", width=30)
            sem12.place(x=1000, y=240)
            Label(root, text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=240)

            sem13=Entry(root, textvariable=sem3, bg="light sky blue", width=30)
            sem13.place(x=1000, y=280)
            Label(root, text="3rd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=280)

            sem14=Entry(root, textvariable=sem4, bg="light sky blue", width=30)
            sem14.place(x=1000, y=320)
            Label(root, text="4th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=320)

            sem15=Entry(root, textvariable=sem5, bg="light sky blue", width=30)
            sem15.place(x=1000, y=360)
            Label(root, text="5th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=360)

            sem16=Entry(root, textvariable=sem6, bg="light sky blue", width=30)
            sem16.place(x=1000, y=400)
            Label(root, text="6th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=400)

            sem17=Entry(root, textvariable=sem7, bg="light sky blue", width=30)
            sem17.place(x=1000, y=440)
            Label(root, text="7th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=440)
        elif combobox.get() == "8th Semester":
            sem11=Entry(root, textvariable=sem1, bg="light sky blue", width=30)
            sem11.place(x=1000, y=200)
            Label(root, text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=200)

            sem12=Entry(root, textvariable=sem2, bg="light sky blue", width=30)
            sem12.place(x=1000, y=240)
            Label(root, text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=240)

            sem13=Entry(root, textvariable=sem3, bg="light sky blue", width=30)
            sem13.place(x=1000, y=280)
            Label(root, text="3rd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=280)

            sem14=Entry(root, textvariable=sem4, bg="light sky blue", width=30)
            sem14.place(x=1000, y=320)
            Label(root, text="4th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=320)

            sem15=Entry(root, textvariable=sem5, bg="light sky blue", width=30)
            sem15.place(x=1000, y=360)
            Label(root, text="5th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=360)

            sem16=Entry(root, textvariable=sem6, bg="light sky blue", width=30)
            sem16.place(x=1000, y=400)
            Label(root, text="6th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=400)

            sem17=Entry(root, textvariable=sem7, bg="light sky blue", width=30)
            sem17.place(x=1000, y=440)
            Label(root, text="7th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=440)

            sem18=Entry(root, textvariable=sem8, bg="light sky blue", width=30)
            sem18.place(x=1000, y=480)
            Label(root, text="8th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(
                x=700, y=480)

    def close():
        root.destroy()

    def nextpage():
        root.destroy()
        # import Display

    root = Tk()
    # root.maxsize(1000, 900)
    root.geometry("1366x768")
    root.title("Data Visualization")
    root.configure(background="sky blue")
    root.minsize(1500, 1600)

    f2 = Frame(root, bg="blue", borderwidth=20, relief=SUNKEN)
    f2.pack(side=LEFT, fill=Y, anchor=W)
    f3 = Frame(root, bg="blue", borderwidth=20, relief=SUNKEN)
    f3.pack(side=RIGHT, fill=Y, anchor=E)
    f3 = Frame(root, bg="blue", borderwidth=20, relief=SUNKEN)
    f3.pack(side=BOTTOM, fill=X, anchor=S)
    f1 = Frame(root, bg="blue", borderwidth=6, relief=SUNKEN)
    f1.pack(side=TOP, fill=X, anchor=W)
    l = Label(f1, text="Data Entry", fg="white", bg="blue", font=" Franklin 12 bold", pady=5)
    l.pack(pady=5, anchor=W)

    Label(root, text="Name", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=7).place(x=100, y=100)
    Label(root, text="Father's Name", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=7).place(x=100,
                                                                                                             y=150)
    Label(root, text="Age", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=7).place(x=100, y=200)
    Label(root, text="Address", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=7).place(x=100, y=250)
    Label(root, text="Mobile Number", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=7).place(x=100,
                                                                                                             y=300)
    Label(root, text="University Number", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=7).place(x=100,
                                                                                                                 y=350)
    Label(root, text="Degree", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=7).place(x=100, y=400)
    Label(root, text="Branch", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=7).place(x=100, y=450)
    Label(root, text="Year", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=7).place(x=100, y=500)
    Label(root, text="12th Marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=7).place(x=700, y=100)
    Label(root, text="10th Marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=7).place(x=100, y=550)
    l = Label(root, text="Semester", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=7).place(x=700,
                                                                                                            y=150)

    name=Entry(root, bg="light sky blue", width=30)
    name.place(x=430, y=110)
    father=Entry(root,  bg="light sky blue", width=30)
    father.place(x=430, y=160)
    age=Entry(root,bg="light sky blue", width=30)
    age.place(x=430, y=210)
    address=Entry(root,  bg="light sky blue", width=30)
    address.place(x=430, y=260)
    mobile=Entry(root, bg="light sky blue", width=30)
    mobile.place(x=430, y=310)
    Id=Entry(root, bg="light sky blue", width=30)
    Id.place(x=430, y=360)
    degree=Entry(root,  bg="light sky blue", width=30)
    degree.place(x=430, y=410)
    branch=Entry(root,  bg="light sky blue", width=30)
    branch.place(x=430, y=460)
    year=Entry(root,  bg="light sky blue", width=30)
    year.place(x=430, y=510)
    mark10=Entry(root,  bg="light sky blue", width=30)
    mark10.place(x=1000, y=110)
    mark12=Entry(root,  bg="light sky blue", width=30)
    mark12.place(x=430, y=560)
    sem1 = IntVar()
    sem2 = IntVar()
    sem3 = IntVar()
    sem4 = IntVar()
    sem5 = IntVar()
    sem6 = IntVar()
    sem7 = IntVar()
    sem8 = IntVar()

    Button(root, text="Submit", command=dataframe, bg="light sky blue", fg="Blue", font="Franklin 12 bold").place(x=550,
                                                                                                                  y=610)
    Button(root, text="Clear", command=Clearvalue, bg="light sky blue", fg="Blue", font="Franklin 12 bold").place(x=650,
                                                                                                                  y=610)
    Button(root, text="Next", command=nextpage, bg="light sky blue", fg="Blue", font="Franklin 12 bold").place(x=450,
                                                                                                               y=610)

    obj = Clearvalue()

    combovalue = StringVar()
    combobox = ttk.Combobox(root, textvariable=combovalue, background="light sky blue")
    semester = (
    "1st Semester", "2nd Semester", "3rd Semester", "4th Semester", "5th Semester", "6th Semester", "7th Semester",
    "8th Semester")
    combobox['values'] = semester
    combobox['state'] = 'readonly'
    combobox.place(x=1000, y=155)
    combobox.bind('<<ComboboxSelected>>', semesterbox)

    root.mainloop()

def displayfunction():

    def reset():
        for record in tree.get_children():
            tree.delete(record)
        conn = sqlite3.connect('datavisual.db')
        c = conn.cursor()
        c.execute("SELECT  * FROM datavalue")
        records = c.fetchall()
        print(records)
        cout=0
        for i in records:
            if cout % 2 == 0:
                tree.insert('', END, values=i, tag=('evenrow',))
            else:
                tree.insert('', END, values=i, tag=('oddrow',))
            cout += 1
        conn.commit()
        conn.close()

    def back():
        root.destroy()
        updatefunction()


    root = Tk()
    # root.maxsize(1000, 900)
    root.minsize(1500, 1600)
    root.geometry("1366x768")
    root.title("Data Visualization")
    root.configure(background="#7FB3D5")
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background='sky blue')
    style.map('Treeview', background=[('selected', 'green')])

    mainmenu = Menu(root)
    m1 = Menu(root, tearoff=0)
    m1.add_command(label="Reset", command=reset)
    m1.add_command(label="Back",command=back)
    m1.add_separator()
    m1.add_command(label="Exit ", command=root.quit)
    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="File", menu=m1)



    def clear():
        with open('Data.txt', 'w') as f:
            f.truncate(0)

    def view():
        root.destroy()
        rowfunction()
        clear()

    def item_selected(event):
        rowvalue = []
        curritem = tree.focus()
        l1 = Label(f3, text=f"{curritem} item selected ", font="Franklin 11 bold", bg="#4C787E").place(x=1000,y=10)
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

    def selectrecord():
        item = tree.focus()
        value = tree.item(item, "values")
        print(value)
        names.delete(0, END)
        father.delete(0, END)
        age.delete(0, END)
        address.delete(0, END)
        mobile.delete(0, END)
        Id.delete(0, END)
        degree.delete(0, END)
        branch.delete(0, END)
        year.delete(0, END)
        mark10.delete(0, END)
        mark12.delete(0, END)
        sem1.delete(0, END)
        sem2.delete(0, END)
        sem3.delete(0, END)
        sem4.delete(0, END)
        sem5.delete(0, END)
        sem6.delete(0, END)
        sem7.delete(0, END)
        sem8.delete(0, END)
        names.insert(0, value[0])
        father.insert(0, value[1])
        age.insert(0, value[2])
        address.insert(0, value[3])
        mobile.insert(0, value[4])
        Id.insert(0, value[5])
        degree.insert(0, value[6])
        branch.insert(0, value[7])
        year.insert(0, value[8])
        mark10.insert(0, value[9])
        mark12.insert(0, value[10])
        sem1.insert(0, value[11])
        sem2.insert(0, value[12])
        sem3.insert(0, value[13])
        sem4.insert(0, value[14])
        sem5.insert(0, value[15])
        sem6.insert(0, value[16])
        sem7.insert(0, value[17])
        sem8.insert(0, value[18])

    def Updaterecord():
        # Grab the record number
        selected = tree.focus()
        # Update record
        tree.item(selected, text="", values=(names.get(),father.get(),age.get(),address.get(),mobile.get(),Id.get(),degree.get(),branch.get(),mark10.get()
                                             ,mark12.get(),sem1.get(),sem2.get(),sem3.get(),sem4.get(),sem5.get(),sem6.get(),sem7.get(),sem8.get()))

        # Create a database or connect to one that exists
        conn = sqlite3.connect('datavisual.db')

        # Create a cursor instance
        c = conn.cursor()

        c.execute("""UPDATE datavalue SET 
            Sname=:name ,fathername=:father,age=:age,address=:address,mobile=:mobile,degree=:degree,branch=:branch,year=:year
            ,mark10=:mark10,mark12=:mark12,sem1=:sem1,sem2=:sem2,sem3=:sem3,sem4=:sem4,sem5=:sem5,sem6=:sem6,sem7=:sem7,sem8=:sem8        
        WHERE id="""+Id.get(),
                  {
                    'name':names.get(),'father':father.get(),'age':age.get(),'address':address.get(),'mobile':mobile.get(),'id':Id.get(),'degree':degree.get(),
                      'branch':branch.get(),'year':year.get(),'mark10':mark10.get(),'mark12':mark12.get(),'sem1':sem1.get(),'sem2':sem2.get(),'sem3':sem3.get()
                      , 'sem4': sem4.get(),'sem5':sem5.get(),'sem6':sem6.get(),'sem7':sem7.get(),'sem8':sem8.get()


                  })

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()
        names.delete(0, END)
        father.delete(0, END)
        age.delete(0, END)
        address.delete(0, END)
        mobile.delete(0, END)
        Id.delete(0, END)
        degree.delete(0, END)
        branch.delete(0, END)
        year.delete(0, END)
        mark10.delete(0, END)
        mark12.delete(0, END)
        sem1.delete(0, END)
        sem2.delete(0, END)
        sem3.delete(0, END)
        sem4.delete(0, END)
        sem5.delete(0, END)
        sem6.delete(0, END)
        sem7.delete(0, END)
        sem8.delete(0, END)

    def deleterecord():
        x = tree.selection()[0]
        tree.delete(x)

        # Create a database or connect to one that exists
        conn = sqlite3.connect('datavisual.db')

        # Create a cursor instance
        c = conn.cursor()

        # Delete From Database
        c.execute("DELETE from datavalue WHERE id=" + Id.get())

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()
        clear()
        names.delete(0, END)
        father.delete(0, END)
        age.delete(0, END)
        address.delete(0, END)
        mobile.delete(0, END)
        Id.delete(0, END)
        degree.delete(0, END)
        branch.delete(0, END)
        year.delete(0, END)
        mark10.delete(0, END)
        mark12.delete(0, END)
        sem1.delete(0, END)
        sem2.delete(0, END)
        sem3.delete(0, END)
        sem4.delete(0, END)
        sem5.delete(0, END)
        sem6.delete(0, END)
        sem7.delete(0, END)
        sem8.delete(0, END)
        tmsg.showinfo("Deleted","Record has been Deleted")


    Frame(root, bg="#348781", borderwidth=30, relief=SUNKEN).pack(side=LEFT, fill=Y, anchor=W)
    Frame(root, bg="#348781", borderwidth=30, relief=SUNKEN).pack(side=RIGHT, fill=Y, anchor=E)
    Frame(root, bg="#348781", borderwidth=30, relief=SUNKEN).pack(side=BOTTOM, fill=X, anchor=S)
    f1 = Frame(root, bg="#348781", borderwidth=6, relief=SUNKEN)
    f1.pack(side=TOP, fill=X, anchor=W)
    Label(f1, text="Data Table View", fg="black", bg="#348781", font=" Franklin 15 bold", pady=5).pack(pady=5, anchor=W)

    col = ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11', '#12', '#13', '#14', '#15', '#16', '#17', '#18','#19')
    file = pd.read_csv('Data analysis')
    f = ttk.Labelframe(root, text="Data Table")
    f.place(x=20, y=80, height=300, width=1470)
    tree = ttk.Treeview(f, columns=col, show='headings')
    tree.pack(padx=20, pady=10, anchor=CENTER, fill=X)
    tree.bind('<ButtonRelease-1>',item_selected)
    tree.tag_configure('oddrow', background='white')
    tree.tag_configure('evenrow', background='sky blue')

    scrollx = Scrollbar(f, orient=HORIZONTAL, command=tree.xview)
    scrolly = Scrollbar(f, orient=VERTICAL, command=tree.yview)
    tree.configure(xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
    scrollx.pack(side=BOTTOM, fill=X)
    scrolly.pack(side=RIGHT, fill=Y, anchor=N)

    # headings

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
    cout = 0
    conn = sqlite3.connect('datavisual.db')
    c = conn.cursor()
    c.execute("SELECT  * FROM datavalue")
    records = c.fetchall()
    print(records)
    for i in records:
        if cout % 2 == 0:
            tree.insert('', END, values=i, tag=('evenrow',))
        else:
            tree.insert('', END, values=i, tag=('oddrow',))
        cout += 1
    conn.commit()
    conn.close()

    f2 = LabelFrame(root, text="Record", relief=RIDGE)
    f2.place(x=20, y=400, height=250, width=1470)

    # labels
    Label(f2, text="Name", fg="black", font=" Franklin 9 bold", pady=5).place(x=20, y=10)
    Label(f2, text="Father\'s Name", fg="black", font=" Franklin 9 bold", pady=5).place(x=20, y=30)
    Label(f2, text="Age", fg="black", font=" Franklin 9 bold", pady=5).place(x=20, y=50)
    Label(f2, text="Address", fg="black", font=" Franklin 9 bold", pady=5).place(x=20, y=70)
    Label(f2, text="Mobile number", fg="black", font=" Franklin 9 bold", pady=5).place(x=20, y=90)
    Label(f2, text="University Id", fg="black", font=" Franklin 9 bold", pady=5).place(x=20, y=110)
    Label(f2, text="Degree", fg="black", font=" Franklin 9 bold", pady=5).place(x=20, y=130)
    Label(f2, text="Branch", fg="black", font=" Franklin 9 bold", pady=5).place(x=20, y=150)
    Label(f2, text="Year", fg="black", font=" Franklin 9 bold", pady=5).place(x=20, y=170)
    Label(f2, text="10th marks", fg="black", font=" Franklin 9 bold", pady=5).place(x=20, y=190)

    Label(f2, text="12th marks", fg="black", font=" Franklin 9 bold", pady=5).place(x=700, y=10)
    Label(f2, text="1st semester", fg="black", font=" Franklin 9 bold", pady=5).place(x=700, y=30)
    Label(f2, text="2nd semester", fg="black", font=" Franklin 9 bold", pady=5).place(x=700, y=50)
    Label(f2, text="3rd semester", fg="black", font=" Franklin 9 bold", pady=5).place(x=700, y=70)
    Label(f2, text="4th semester", fg="black", font=" Franklin 9 bold", pady=5).place(x=700, y=90)
    Label(f2, text="5th semester", fg="black", font=" Franklin 9 bold", pady=5).place(x=700, y=110)
    Label(f2, text="6th semester", fg="black", font=" Franklin 9 bold", pady=5).place(x=700, y=130)
    Label(f2, text="7th semester", fg="black", font=" Franklin 9 bold", pady=5).place(x=700, y=150)
    Label(f2, text="8th semester", fg="black", font=" Franklin 9 bold", pady=5).place(x=700, y=170)

    # entry boxes
    names = Entry(f2)
    names.place(x=180, y=13, height=15)
    father = Entry(f2)
    father.place(x=180, y=33, height=15)
    age = Entry(f2)
    age.place(x=180, y=53, height=15)
    address = Entry(f2)
    address.place(x=180, y=73, height=15)
    mobile = Entry(f2)
    mobile.place(x=180, y=93, height=15)
    Id = Entry(f2)
    Id.place(x=180, y=113, height=15)
    degree = Entry(f2)
    degree.place(x=180, y=133, height=15)
    branch = Entry(f2)
    branch.place(x=180, y=153, height=15)
    year = Entry(f2)
    year.place(x=180, y=173, height=15)
    mark10 = Entry(f2)
    mark10.place(x=180, y=193, height=15)
    mark12 = Entry(f2)
    mark12.place(x=900, y=13, height=15)
    sem1 = Entry(f2)
    sem1.place(x=900, y=33, height=15)
    sem2 = Entry(f2)
    sem2.place(x=900, y=53, height=15)
    sem3 = Entry(f2)
    sem3.place(x=900, y=73, height=15)
    sem4 = Entry(f2)
    sem4.place(x=900, y=93, height=15)
    sem5 = Entry(f2)
    sem5.place(x=900, y=113, height=15)
    sem6 = Entry(f2)
    sem6.place(x=900, y=133, height=15)
    sem7 = Entry(f2)
    sem7.place(x=900, y=153, height=15)
    sem8 = Entry(f2)
    sem8.place(x=900, y=173, height=15)

    # Buttons
    f3 = LabelFrame(root, text="Commands")
    f3.place(x=20, y=670, height=80, width=1470)
    Button(f3, text="Select Record", command=selectrecord).place(x=10, y=10)
    Button(f3, text="Update Record", command=Updaterecord).place(x=120, y=10)
    Button(f3, text="Delete Record", command=deleterecord).place(x=230, y=10)
    Button(f3, text="View Record", command=view).place(x=340, y=10)

    def up():
        rows = tree.selection()
        for row in rows:
            tree.move(row, tree.parent(row), tree.index(row) - 1)

    Button(f3, text="Move up", command=up).place(x=450, y=10)

    def down():
        rows = tree.selection()
        for row in reversed(rows):
            tree.move(row, tree.parent(row), tree.index(row) + 1)

    Button(f3, text="Move Down", command=down).place(x=550, y=10)

    def remove_one():
        x = tree.selection()[0]
        tree.delete(x)

    Button(f3, text="Remove", command=remove_one).place(x=660, y=10)

    root.mainloop()

def rowfunction():

    def mypopup(event):
        menu.tk_popup(event.x_root,event.y_root)

    def nextpage():
        root.destroy()
        updatefunction()
        # import update

    def home():
        root.destroy()
        updatefunction()
    l = []
    with open('Data.txt', 'r') as f:

        for i in f:
            i = i.split(',')
            l.append(i)
    root = Tk()
    root.geometry('1366x768')
    root.title('Visulisation')
    root.configure(background="Aliceblue")

    menu=Menu(root,tearoff=False)
    menu.add_command(label="Home",command=home)
    menu.add_command(label="Back", command=nextpage)
    menu.add_command(label="Exit",command=exit)
    root.bind('<Button-3>',mypopup)
# label frame values
    labelframe = LabelFrame(root, text="Student Name", width=200, height=200, bg="light blue", fg="black",font="Castellar 12 bold")
    labelframe.place(x=10, y=20, height=60, width=200)

    name = l[0][0]
    print(name)
    Label(labelframe, text=name, font="Arial 15 bold", bg="light blue").pack()

    labelframe = LabelFrame(root, text="Father\'s Name", bg="light blue", fg="black", font="Castellar 12 bold")
    labelframe.place(x=300, y=20, height=60, width=200)
    name = l[0][1]
    print(name)
    Label(labelframe, text=name, font="Arial 15 bold", bg="light blue").pack()

    labelframe = LabelFrame(root, text="AGE", bg="light blue", fg="black", font="Castellar 12 bold")
    labelframe.place(x=600, y=20, height=60, width=200)
    name = l[0][2]
    print(name)
    Label(labelframe, text=name, font="Arial 15 bold", bg="light blue").pack()

    labelframe = LabelFrame(root, text="University Number", bg="light blue", fg="black", font="Castellar 12 bold")
    labelframe.place(x=900, y=20, height=60, width=300)
    name = l[0][5]
    print(name)
    Label(labelframe, text=name, font="Arial 15 bold", bg="light blue").pack()

    labelframe = LabelFrame(root, text="Year", bg="light blue", fg="black", font="Castellar 12 bold")
    labelframe.place(x=1300, y=20, height=60, width=200)
    name = l[0][8]
    print(name)
    Label(labelframe, text=name, font="Arial 15 bold", bg="light blue").pack()

    labelframe = LabelFrame(root, text="Address", bg="light blue", fg="black", font="Castellar 12 bold")
    labelframe.place(x=10, y=100, height=60, width=490)
    name = l[0][3]
    print(name)
    Label(labelframe, text=name, font="Arial 15 bold", bg="light blue").pack()

    labelframe = LabelFrame(root, text="Mobile Number", bg="light blue", fg="black", font="Castellar 12 bold")
    labelframe.place(x=600, y=100, height=60, width=300)
    name = l[0][4]
    print(name)
    Label(labelframe, text=name, font="Arial 15 bold", bg="light blue").pack()

    labelframe = LabelFrame(root, text="Course", bg="light blue", fg="black", font="Castellar 12 bold")
    labelframe.place(x=1000, y=100, height=60, width=200)
    name = l[0][6]
    print(name)
    Label(labelframe, text=name, font="Arial 15 bold", bg="light blue").pack()

    labelframe = LabelFrame(root, text="Branch", bg="light blue", fg="black", font="Castellar 12 bold")
    labelframe.place(x=1300, y=100, height=60, width=200)
    name = l[0][7]
    print(name)
    Label(labelframe, text=name, font="Arial 15 bold", bg="light blue").pack()

    # this list contains semester marks
    semmarks = []
    for i in range(11, 19):
        semmarks.append(int(l[0][i]))
    print(semmarks)

    figure2 = Figure(figsize=(4, 3), dpi=100)
    subplot2 = figure2.add_subplot(111)
    labels2 = 'High School', 'Intermideate'
    pieSizes = [l[0][9], l[0][10]]
    my_colors2 = ['lightblue', 'lightsteelblue']
    explode2 = (0, 0.1)
    subplot2.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90)
    subplot2.axis('equal')
    pie2 = FigureCanvasTkAgg(figure2, root)
    pie2.get_tk_widget().place(x=80, y=200, height=500, width=700)

    if len(semmarks)==8:
        Index = ['Sem1', 'Sem2', 'Sem3', 'Sem4', 'Sem5', 'Sem6', 'Sem7', 'Sem8']
        df = {"Marks": semmarks, "Semester": Index}
        df1 = pd.DataFrame(df)
        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().place(x=800, y=200, height=500, width=700)
        df1.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=10)
        ax1.set_title('Semester marks')
    elif len(semmarks)==7:
        Index = ['Sem1', 'Sem2', 'Sem3', 'Sem4', 'Sem5', 'Sem6', 'Sem7']
        df = {"Marks": semmarks, "Semester": Index}
        df1 = pd.DataFrame(df)
        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().place(x=800, y=200, height=500, width=700)
        df1.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=10)
        ax1.set_title('Semester marks')
    elif len(semmarks)==6:
        Index = ['Sem1', 'Sem2', 'Sem3', 'Sem4', 'Sem5', 'Sem6']
        df = {"Marks": semmarks, "Semester": Index}
        df1 = pd.DataFrame(df)
        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().place(x=800, y=200, height=500, width=700)
        df1.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=10)
        ax1.set_title('Semester marks')
    elif len(semmarks)==5:
        Index = ['Sem1', 'Sem2', 'Sem3', 'Sem4', 'Sem5']
        df = {"Marks": semmarks, "Semester": Index}
        df1 = pd.DataFrame(df)
        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().place(x=800, y=200, height=500, width=700)
        df1.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=10)
        ax1.set_title('Semester marks')
    elif len(semmarks)==4:
        Index = ['Sem1', 'Sem2', 'Sem3', 'Sem4']
        df = {"Marks": semmarks, "Semester": Index}
        df1 = pd.DataFrame(df)
        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().place(x=800, y=200, height=500, width=700)
        df1.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=10)
        ax1.set_title('Semester marks')
    elif len(semmarks)==3:
        Index = ['Sem1', 'Sem2', 'Sem3']
        df = {"Marks": semmarks, "Semester": Index}
        df1 = pd.DataFrame(df)
        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().place(x=800, y=200, height=500, width=700)
        df1.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=10)
        ax1.set_title('Semester marks')
    elif len(semmarks)==2:
        Index = ['Sem1', 'Sem2']
        df = {"Marks": semmarks, "Semester": Index}
        df1 = pd.DataFrame(df)
        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().place(x=800, y=200, height=500, width=700)
        df1.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=10)
        ax1.set_title('Semester marks')
    elif len(semmarks)==1:
        Index = ['Sem1']
        df = {"Marks": semmarks, "Semester": Index}
        df1 = pd.DataFrame(df)
        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().place(x=800, y=200, height=500, width=700)
        df1.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=10)
        ax1.set_title('Semester marks')




    root.mainloop()

def updatefunction():
    root = Tk()
    root.geometry("1000x700")
    root.configure(background='#C39BD3')

    f1 = Frame(root, bg="#F5B7B1", borderwidth=4, relief=SUNKEN)
    f1.pack(side=TOP, fill=X, anchor=W)
    l = Label(f1, text="Data Analysis and Visualization", fg="#34495E", bg="#F5B7B1", font=" Franklin 15 bold",pady=5)
    l.pack(anchor=NW)

    can=Canvas(root,height=220,width=200,bg="#D2B4DE")
    can.place(x=100,y=160)

    im = Image.open("add.png")
    im = im.resize((90,90), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(im)
    can.create_image(100,90,image=img)

    cann=Canvas(root,height=220,width=200,bg="#D2B4DE")
    cann.place(x=450,y=160)

    im = Image.open('display.png')
    im = im.resize((90,90), Image.ANTIALIAS)
    imgi = ImageTk.PhotoImage(im)
    cann.create_image(100,90,image=imgi)

    im=Image.open("bg.jpg")
    ph=ImageTk.PhotoImage(im)
    # l=ttk.Labelframe(root)
    # l.place(x=0,y=0,height=100,width=1600,anchor=NW)
    # ll=Label(l,image=ph)
    # ll.pack(fill=X)

    def add():
        svar.set("wait......")
        sbar.update()
        import time
        time.sleep(2)
        svar.set("Sucessful.....")
        root.destroy()
        datafunction()
        # import Entrypage
        # Entrypage.root.destroy()

    def disp():
        svar.set("wait......")
        sbar.update()
        import time
        time.sleep(2)
        svar.set("Sucessful.....")
        root.destroy()
        displayfunction()

    svar=StringVar()
    svar.set("Running...")
    sbar=Label(textvariable=svar,relief=RIDGE,anchor=W,bg="#D2B4DE")
    sbar.pack(side=BOTTOM,fill=X)

    b1=Button(root, text="Add Record", command=add,bg="#D2B4DE",fg="#4A235A",font="Franklin 10 bold").place(x=155,y=305)
    b2=Button(root, text="Display Record", command=disp,bg="#D2B4DE",fg="#4A235A",font="Franklin 10 bold").place(x=500,y=305)

    root.mainloop()

if __name__ == '__main__':

    sign()