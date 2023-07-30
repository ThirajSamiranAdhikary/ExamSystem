import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import mysql.connector

#to register admin user and normal user
class ad:
    def __init__(self):
        self.mycursor=''
        self.mydb=''
        self.root = tk.Tk()
        self.root.geometry("550x300")
        self.root.title("User Register")
        self.f3 = tk.Frame(self.root, bg='green')
        self.f3.place(x=0, y=0, width=550, height=300)
        self.b3 = tk.Button(self.f3, text="Register User", bg='blue',command=self.registerUsers)
        self.b3.place(x=250, y=200, width=100, height=50)

        self.b4 = tk.Button(self.f3, text="Exit", bg='red',command=self.root.destroy)
        self.b4.place(x=125, y=200, width=100, height=50)

        self.l4 = tk.Label(self.f3, text='Enter User Name:')
        self.l4.place(x=50, y=50)
        self.e3 = tk.Entry(self.f3, width=25, font=("", 12))
        self.e3.place(x=200, y=50)

        #user type
        self.op=['Admin','User']
        self.dd=ttk.Combobox(self.root,values=self.op)
        self.dd.current(0)
        self.l6 = tk.Label(self.f3, text='Enter User Type:')
        self.l6.place(x=50, y=100)
        self.dd.place(x=200, y=100)

        self.l6 = tk.Label(self.f3, text='Enter Password:')
        self.l6.place(x=50, y=150)
        self.e5= tk.Entry(self.f3, width=25, font=("", 12))
        self.e5.place(x=200, y=150)

        self.root.mainloop()

    def registerUsers(self):
        self.name = self.e3.get()
        self.pw=int(self.e5.get())
        self.type=self.dd.get()
        self.databseConnection()
        self.mycursor=self.mydb.cursor()
        self.sql="insert into users(userName,userType,password) values(%s,%s,%s)"
        self.val=(self.name,self.type,self.pw)
        self.mycursor.execute(self.sql,self.val)
        self.mydb.commit()
        tkinter.messagebox.showinfo("Message",'User upload into Database')

    def databseConnection(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="mydb"
            )

        except:
            tkinter.messagebox.showinfo("Message", "Error connection")





