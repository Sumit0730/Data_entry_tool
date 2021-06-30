from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tmsg

def sign():
    def nextPage():
        root.destroy()
        import update

    global value
    def getvalue():

        print(uservalue.get())
        print(passvalue.get())
        # with open("record.txt", "a") as f:
        #     f.write(f"{uservalue.get(), passvalue.get(), ckvalue.get()}\n")
        if uservalue.get() != "admin":
            tmsg.showerror("Error", "Invalid username")
        elif passvalue.get() != "admin":
            tmsg.showerror("Error", "Invalid password")
        else:
            value=tmsg.showinfo("Login Successfully", "Press OK to continue")
            print(value)
            if value == "ok":
                bt = Button(text="Next", command=nextPage, bg="#7CFC00", font="Franklin 12 bold").place(x=800, y=600)



    root = Tk()

    root.geometry("1366x768")
    root.minsize(1500,1600)
    f1 = Frame(root, bg="#7CFC00", borderwidth=6, relief=SUNKEN)
    f1.pack(side=TOP, fill=X, anchor=W)
    l = Label(f1, text="Data Analysis and Visualization", fg="black", bg="#7CFC00", font=" Franklin 20 bold",pady=12)
    l.pack(pady=5)

    f2 = Frame(root, bg="#7CFC00", borderwidth=16, relief=SUNKEN)
    f2.pack(side=BOTTOM, fill=X, anchor=S)
    Frame(root, bg="#7CFC00", borderwidth=6, relief=SUNKEN).pack(side=LEFT, fill=X, anchor=W)

    root.title("Data Visualization")
    root.configure(background="black")

    t=Label(text="Username",bg="black",fg="#7CFC00",font=" Franklin 20 bold",pady=10).place(x=500,y=400)
    t=Label(text="Password",bg="black",fg="#7CFC00",font=" Franklin 20 bold",pady=12).place(x=500,y=450)
    uservalue=StringVar()
    passvalue=StringVar()
    userentry=Entry(textvariable=uservalue,bg="#7CFC00",width=25)
    passentry=Entry(textvariable=passvalue,bg="#7CFC00",width=25)
    userentry.place(x=700,y=420)
    passentry.place(x=700,y=470)
    b=Button(text="Login", command=getvalue,bg="#7CFC00",font="Franklin 12 bold").place(x=600,y=600)
    f2=Frame(root, bg="#7CFC00", borderwidth=25, relief=SUNKEN)
    f2.pack(side=LEFT, fill=Y, anchor=W)
    f3 = Frame(root, bg="#7CFC00", borderwidth=25, relief=SUNKEN)
    f3.pack(side=RIGHT, fill=Y, anchor=E)
    ckvalue=IntVar()
    ck=Checkbutton(text=" I am not a Robot",variable=ckvalue,font="Franklin 12 bold",bg="#7CFC00").place(x=600,y=530)
    im=Image.open("login.png")
    im=im.resize((200,200), Image.ANTIALIAS)
    ph=ImageTk.PhotoImage(im)
    l=Label(image=ph,bg="black")
    l.place(x=600,y=150)


    root.mainloop()

if __name__ == '__main__':

    sign()