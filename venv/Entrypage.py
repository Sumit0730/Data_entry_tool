from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.messagebox as tmsg
import pandas as pd


def dataframe(event='<<ComboboxSelected>>'):
    l = []
    l.append(namevalue.get())
    l.append(fathervalue.get())
    l.append(agevalue.get())
    l.append(addressvalue.get())
    l.append(mobilevalue.get())
    l.append(rollnovalue.get())
    l.append(degreevalue.get())
    l.append(branchvalue.get())
    l.append(yearvalue.get())
    l.append(marks10.get())
    l.append(marks12.get())
    if combobox.get()=="1st Semester":
        l.append(sem1.get())
    elif combobox.get()=="2nd Semester":
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
    with open('newdata.txt','a') as ff:
        for i in l:
            ff.write(str(i))
            ff.write(",")
        ff.write("\n")
    # CSV()
    # df=pd.DataFrame(ff)
    # newdf=df.T
    # newdf.to_csv("Data analysis",index=False,header=False)
def datavalue():
    val=tmsg.showinfo("Successful", "Data Uploaded successfully")

    print(namevalue.get())
    print(fathervalue.get())
    print(agevalue.get())
    print(addressvalue.get())
    print(mobilevalue.get())
    print(rollnovalue.get())
    print(degreevalue.get())
    print(branchvalue.get())
    print(yearvalue.get())

    dataframe()
    close()
    import update
def Clearvalue():
    namevalue.set("")
    fathervalue.set("")
    agevalue.set("")
    addressvalue.set("")
    mobilevalue.set("")
    rollnovalue.set("")
    degreevalue.set("")
    branchvalue.set("")
    yearvalue.set("")
    marks12.set("")
    marks10.set("")
    sem1.set("")
    sem2.set("")
    sem3.set("")
    sem4.set("")
    sem5.set("")
    sem6.set("")
    sem7.set("")
    sem8.set("")
def semesterbox(event):
    if combobox.get()=="1st Semester":
        Entry(root,textvariable=sem1, bg="light sky blue", width=30).place(x=1000, y=200)
        Label(root,text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=200)

    elif combobox.get()=="2nd Semester":
        Entry(root,textvariable=sem1, bg="light sky blue", width=30).place(x=1000, y=200)
        Label(root,text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=200)

        Entry(root,textvariable=sem2, bg="light sky blue", width=30).place(x=1000, y=240)
        Label(root,text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=240)
    elif combobox.get()=="3rd Semester":
        Entry(root,textvariable=sem1, bg="light sky blue", width=30).place(x=1000, y=200)
        Label(root,text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=200)

        Entry(root,textvariable=sem2, bg="light sky blue", width=30).place(x=1000, y=240)
        Label(root,text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=240)

        Entry(root,textvariable=sem3, bg="light sky blue", width=30).place(x=1000, y=280)
        Label(root,text="3rd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=280)
    elif combobox.get() == "4th Semester":
        Entry(root,textvariable=sem1, bg="light sky blue", width=30).place(x=1000, y=200)
        Label(root,text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=200)

        Entry(root,textvariable=sem2, bg="light sky blue", width=30).place(x=1000, y=240)
        Label(root,text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=240)

        Entry(root,textvariable=sem3, bg="light sky blue", width=30).place(x=1000, y=280)
        Label(root,text="3rd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=280)

        Entry(root,textvariable=sem4, bg="light sky blue", width=30).place(x=1000, y=320)
        Label(root,text="4th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=320)
    elif combobox.get() == "5th Semester":
        Entry(root,textvariable=sem1, bg="light sky blue", width=30).place(x=1000, y=200)
        Label(root,text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=200)

        Entry(root,textvariable=sem2, bg="light sky blue", width=30).place(x=1000, y=240)
        Label(root,text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=240)

        Entry(root,textvariable=sem3, bg="light sky blue", width=30).place(x=1000, y=280)
        Label(root,text="3rd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=280)

        Entry(root,textvariable=sem4, bg="light sky blue", width=30).place(x=1000, y=320)
        Label(root,text="4th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=320)

        Entry(root,textvariable=sem5, bg="light sky blue", width=30).place(x=1000, y=360)
        Label(root,text="5th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=360)
    elif combobox.get() == "6th Semester":
        Entry(root,textvariable=sem1, bg="light sky blue", width=30).place(x=1000, y=200)
        Label(root,text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=200)

        Entry(root,textvariable=sem2, bg="light sky blue", width=30).place(x=1000, y=240)
        Label(root,text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=240)

        Entry(root,textvariable=sem3, bg="light sky blue", width=30).place(x=1000, y=280)
        Label(root,text="3rd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=280)

        Entry(root,textvariable=sem4, bg="light sky blue", width=30).place(x=1000, y=320)
        Label(root,text="4th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=320)

        Entry(root,textvariable=sem5, bg="light sky blue", width=30).place(x=1000, y=360)
        Label(root,text="5th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=360)

        Entry(root,textvariable=sem6, bg="light sky blue", width=30).place(x=1000, y=400)
        Label(root,text="6th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=400)
    elif combobox.get() == "7th Semester":
        Entry(root,textvariable=sem1, bg="light sky blue", width=30).place(x=1000, y=200)
        Label(root,text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=200)

        Entry(root,textvariable=sem2, bg="light sky blue", width=30).place(x=1000, y=240)
        Label(root,text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=240)

        Entry(root,textvariable=sem3, bg="light sky blue", width=30).place(x=1000, y=280)
        Label(root,text="3rd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=280)

        Entry(root,textvariable=sem4, bg="light sky blue", width=30).place(x=1000, y=320)
        Label(root,text="4th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=320)

        Entry(root,textvariable=sem5, bg="light sky blue", width=30).place(x=1000, y=360)
        Label(root,text="5th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=360)

        Entry(root,textvariable=sem6, bg="light sky blue", width=30).place(x=1000, y=400)
        Label(root,text="6th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=400)

        Entry(root,textvariable=sem7, bg="light sky blue", width=30).place(x=1000, y=440)
        Label(root,text="7th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=440)
    elif combobox.get() == "8th Semester":
        Entry(root,textvariable=sem1, bg="light sky blue", width=30).place(x=1000, y=200)
        Label(root,text="1st Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=200)

        Entry(root,textvariable=sem2, bg="light sky blue", width=30).place(x=1000, y=240)
        Label(root,text="2nd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=240)

        Entry(root,textvariable=sem3, bg="light sky blue", width=30).place(x=1000, y=280)
        Label(root,text="3rd Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=280)

        Entry(root,textvariable=sem4, bg="light sky blue", width=30).place(x=1000, y=320)
        Label(root,text="4th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=320)

        Entry(root,textvariable=sem5, bg="light sky blue", width=30).place(x=1000, y=360)
        Label(root,text="5th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=360)

        Entry(root,textvariable=sem6, bg="light sky blue", width=30).place(x=1000, y=400)
        Label(root,text="6th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=400)

        Entry(root,textvariable=sem7, bg="light sky blue", width=30).place(x=1000, y=440)
        Label(root,text="7th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=440)

        Entry(root,textvariable=sem8, bg="light sky blue", width=30).place(x=1000, y=480)
        Label(root,text="8th Sem marks", bg="sky blue", fg="dark blue", font=" Franklin 13 bold", pady=5).place(x=700, y=480)
def close():
    root.destroy()
def nextpage():
    root.destroy()
    import Display

root = Tk()
# root.maxsize(1000, 900)
root.geometry("1366x768")
root.title("Data Visualization")
root.configure(background="sky blue")
root.minsize(1500,1600)

f2 = Frame(root, bg="blue", borderwidth=20, relief=SUNKEN)
f2.pack(side=LEFT, fill=Y, anchor=W)
f3 = Frame(root, bg="blue", borderwidth=20, relief=SUNKEN)
f3.pack(side=RIGHT, fill=Y, anchor=E)
f3 = Frame(root, bg="blue", borderwidth=20, relief=SUNKEN)
f3.pack(side=BOTTOM, fill=X, anchor=S)
f1 = Frame(root, bg="blue", borderwidth=6, relief=SUNKEN)
f1.pack(side=TOP, fill=X, anchor=W)
l = Label(f1, text="Data Entry", fg="white", bg="blue", font=" Franklin 12 bold", pady=5)
l.pack(pady=5,anchor=W)

Label(root,text="Name",bg="sky blue",fg="dark blue",font=" Franklin 13 bold",pady=7).place(x=100,y=100)
Label(root,text="Father's Name",bg="sky blue",fg="dark blue",font=" Franklin 13 bold",pady=7).place(x=100,y=150)
Label(root,text="Age",bg="sky blue",fg="dark blue",font=" Franklin 13 bold",pady=7).place(x=100,y=200)
Label(root,text="Address",bg="sky blue",fg="dark blue",font=" Franklin 13 bold",pady=7).place(x=100,y=250)
Label(root,text="Mobile Number",bg="sky blue",fg="dark blue",font=" Franklin 13 bold",pady=7).place(x=100,y=300)
Label(root,text="University Number",bg="sky blue",fg="dark blue",font=" Franklin 13 bold",pady=7).place(x=100,y=350)
Label(root,text="Degree",bg="sky blue",fg="dark blue",font=" Franklin 13 bold",pady=7).place(x=100,y=400)
Label(root,text="Branch",bg="sky blue",fg="dark blue",font=" Franklin 13 bold",pady=7).place(x=100,y=450)
Label(root,text="Year",bg="sky blue",fg="dark blue",font=" Franklin 13 bold",pady=7).place(x=100,y=500)
Label(root,text="12th Marks",bg="sky blue",fg="dark blue",font=" Franklin 13 bold",pady=7).place(x=700,y=100)
Label(root,text="10th Marks",bg="sky blue",fg="dark blue",font=" Franklin 13 bold",pady=7).place(x=100,y=550)
l=Label(root,text="Semester",bg="sky blue",fg="dark blue",font=" Franklin 13 bold",pady=7).place(x=700,y=150)

namevalue = StringVar()
fathervalue = StringVar()
agevalue=IntVar()
addressvalue = StringVar()
mobilevalue=IntVar()
rollnovalue=IntVar()
degreevalue = StringVar()
branchvalue = StringVar()
yearvalue = IntVar()
marks12=IntVar()
marks10=IntVar()
sem1=IntVar()
sem2=IntVar()
sem3=IntVar()
sem4=IntVar()
sem5=IntVar()
sem6=IntVar()
sem7=IntVar()
sem8=IntVar()


Entry(root,textvariable=namevalue,bg="light sky blue",width=30).place(x=430,y=110)
Entry(root,textvariable=fathervalue,bg="light sky blue",width=30).place(x=430,y=160)
Entry(root,textvariable=agevalue,bg="light sky blue",width=30).place(x=430,y=210)
Entry(root,textvariable=addressvalue,bg="light sky blue",width=30).place(x=430,y=260)
Entry(root,textvariable=mobilevalue,bg="light sky blue",width=30).place(x=430,y=310)
Entry(root,textvariable=rollnovalue,bg="light sky blue",width=30).place(x=430,y=360)
Entry(root,textvariable=degreevalue,bg="light sky blue",width=30).place(x=430,y=410)
Entry(root,textvariable=branchvalue,bg="light sky blue",width=30).place(x=430,y=460)
Entry(root,textvariable=yearvalue,bg="light sky blue",width=30).place(x=430,y=510)
Entry(root,textvariable=marks12,bg="light sky blue",width=30).place(x=1000,y=110)
Entry(root,textvariable=marks10,bg="light sky blue",width=30).place(x=430,y=560)


Button(root,text="Submit" ,command=datavalue,bg="light sky blue",fg="Blue",font="Franklin 12 bold").place(x=550,y=610)
Button(root,text="Clear",command=Clearvalue,bg="light sky blue",fg="Blue",font="Franklin 12 bold").place(x=650,y=610)
Button(root,text="Next",command=nextpage,bg="light sky blue",fg="Blue",font="Franklin 12 bold").place(x=450,y=610)

obj=Clearvalue()

combovalue=StringVar()
combobox=ttk.Combobox(root,textvariable=combovalue,background="light sky blue")
semester=("1st Semester","2nd Semester","3rd Semester","4th Semester","5th Semester","6th Semester","7th Semester","8th Semester")
combobox['values']=semester
combobox['state']='readonly'
combobox.place(x=1000,y=155)
combobox.bind('<<ComboboxSelected>>', semesterbox)

root.mainloop()
