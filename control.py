import tkinter as tk
import csv
from ad import ad
from adminwindow import adminwindow

#control panel to Admin user
class control:
    def __init__(self):
        self.c1=ad
        self.a1=adminwindow

        self.root = tk.Tk()
        self.root.geometry("550x300")
        self.root.title("Admin Control Panel")
        self.f3 = tk.Frame(self.root, bg='green')
        self.f3.place(x=0, y=0, width=550, height=300)

        self.b3 = tk.Button(self.f3, text="User Register", bg='blue',command=self.userRegister)
        self.b3.place(x=250, y=100, width=100, height=50)

        self.b4 = tk.Button(self.f3, text="Exit", bg='red',command=self.root.destroy)
        self.b4.place(x=125, y=100, width=100, height=50)

        self.b5 = tk.Button(self.f3, text="Upload Questions", bg='yellow',command=self.uploadQuestion)
        self.b5.place(x=375 , y=100, width=100, height=50)
        self.root.mainloop()


#to swift to user register window
    def userRegister(self):
        self.c1()

#to swift to question upload window
    def uploadQuestion(self):
        self.a1()



