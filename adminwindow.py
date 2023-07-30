import tkinter as tk
import csv
import mysql.connector
import tkinter.messagebox

#to upload questions into databse
class adminwindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("550x300")
        self.root.title("Question Upload")
        self.f3 = tk.Frame(self.root, bg='green')
        self.f3.place(x=0, y=0, width=550, height=300)
        self.b3 = tk.Button(self.f3, text="Upload text File", bg='blue',command=self.uploadQuestions)
        self.b3.place(x=250, y=200, width=100, height=50)

        self.b4 = tk.Button(self.f3, text="Exit", bg='red', command=self.root.destroy)
        self.b4.place(x=125, y=200, width=100, height=50)


        self.l4 = tk.Label(self.f3, text='Enter File Name:')
        self.l4.place(x=50, y=50)
        self.e3 = tk.Entry(self.f3, width=25, font=("", 12))
        self.e3.place(x=200, y=50)
        self.root.mainloop()

    def uploadQuestions(self):
        self.databseConnection()
        self.mycursor=self.mydb.cursor()
        file=self.e3.get()
        try:
            with open(file,'r') as f:
                cv=csv.DictReader(f)
                for i in cv:
                    self.q=i['question']
                    self.an1=i['answer1']
                    self.an2 = i['answer2']
                    self.an3= i['answer3']
                    self.an4 = i['answer4']
                    self.correctAnswer = int(i['correctAnswer'])
                    self.sql="insert into questions(question,answer1,answer2,answer3,answer4,correctAnswer) values(%s,%s,%s,%s,%s,%s)"
                    self.val=(self.q,self.an1,self.an2,self.an3,self.an4,self.correctAnswer)
                    self.mycursor.execute(self.sql,self.val)
                    self.mydb.commit()
                tkinter.messagebox.showinfo("Message","File Uploaded to Database")
        except:
            tkinter.messagebox.showinfo("Error Message","File does not exist")

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


