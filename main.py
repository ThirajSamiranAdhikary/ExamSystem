import tkinter as tk
import tkinter.messagebox
import mysql.connector
from control import control
from questionwindow import questionwindow
import random
import csv
import os

#main window
class GUI:
    def __init__(self):

        self.marks = 0
        self.mycursor=''
        self.a1 = control
        self.q1 = questionwindow

        self.root = tk.Tk()
        self.root.geometry("550x300")
        self.root.title("Logging ")
        self.f1 = tk.Frame(self.root, bg='yellow')
        self.f1.place(x=0, y=0, width=600, height=300)
        # username
        self.l1 = tk.Label(self.f1, text='Enter User Name:')
        self.l1.place(x=50, y=50)
        self.e1 = tk.Entry(self.f1, width=25, font=("", 12))
        self.e1.place(x=200, y=50)
        # password
        self.l2 = tk.Label(self.f1, text='Enter Password:')
        self.l2.place(x=50, y=100)
        self.e2 = tk.Entry(self.f1, width=25, font=("", 12), show='*')
        self.e2.place(x=200, y=100)
        # buttons
        self.b1 = tk.Button(self.f1, text="LogIn", bg='blue',command=self.login)
        self.b1.place(x=250, y=150, width=100, height=50)
        self.b2 = tk.Button(self.f1, text="Exit", command=self.root.destroy, bg='red')
        self.b2.place(x=100, y=150, width=100, height=50)
        self.root.mainloop()

#login function
    def login(self):
        self.name=self.e1.get()
        self.pw=int(self.e2.get())
        self.databseConnection()
        self.userID=[]
        self.username=[]
        self.password=[]
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("select * from users  ")
        for i in self.mycursor:
           self.username.append(i[1])
           self.password.append(i[3])

        self.sql="select userType from users where userName=%s and password=%s"
        self.val=(self.name,str(self.pw))
        self.mycursor.execute(self.sql,self.val)

        self.mytype=self.mycursor.fetchone()

        if self.name in self.username and self.pw in self.password :
            if 'Admin' in self.mytype:
                self.root.destroy()
                self.a1()
            else:
                self.root.destroy()
                self.q1()

        else:
            tkinter.messagebox.showinfo("Error Message","Invalid Login")


#function to connect database
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




g1=GUI()