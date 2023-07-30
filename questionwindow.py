import tkinter as tk
import mysql.connector
import tkinter.messagebox
import random



class questionwindow:
    def __init__(self):
        self.questions = []
        self.answers = []
        self.correctanswers=[]
        self.marks=0
        self.num=9
        self.totalQuestions = 10
        self.x=9
        self.tq=''


        self.root = tk.Tk()
        self.root.geometry("550x400")
        self.root.title("Question WIndow")
        self.f2 = tk.Frame(self.root, bg='green')
        self.f2.place(x=0, y=0, width=550, height=400)
        self.textbox = tk.Text(self.f2, height="10", width="80")
        self.textbox_value = tk.StringVar()
        self.textbox.pack()
        # radio buttons
        self.v = tk.IntVar()
        self.rb1 = tk.Radiobutton(self.f2, text="Option1", variable=self.v, value=1,bg="purple")
        self.rb2 = tk.Radiobutton(self.f2, text="Option2", variable=self.v, value=2,bg="purple")
        self.rb3 = tk.Radiobutton(self.root, text="Option3", variable=self.v, value=3,bg="purple")
        self.rb4 = tk.Radiobutton(self.root, text="Option4", variable=self.v, value=4,bg="purple")
        self.rb1.place(x=100, y=180, width=100, height=50)
        self.rb2.place(x=200, y=180, width=100, height=50)
        self.rb3.place(x=300, y=180, width=100, height=50)
        self.rb4.place(x=400, y=180, width=100, height=50)

        self.start=tk.Button(self.f2,text="Start Quiz",command=self.getQuestionList)
        self.answer = tk.Button(self.f2, text="Correct Answers",command=self.root2)
        self.b7 = tk.Button(self.f2, text="Submit Answers",bg="yellow",command=self.addb)
        self.b6 = tk.Button(self.f2, text="Next",bg="blue",command=self.nextB)
        self.b5 = tk.Button(self.f2, text="Finish",bg="red", command=self.getTotalMark)

        self.l1 = tk.Label(self.root, text='Enter User ID:')
        self.l1.place(x=0, y=310)
        self.e1 = tk.Entry(self.root, width=25, font=("", 12))
        self.e1.place(x=100, y=310)

        self.start.place(x=0, y=250, width=100, height=50)
        self.b7.place(x=120, y=250, width=100, height=50)
        self.b6.place(x=220, y=250, width=100, height=50)
        self.b5.place(x=340, y=310, width=100, height=50)
        self.answer.place(x=450, y=310, width=100, height=50)
        self.textbox.insert(tk.END,"Click Start Quiz Button")
        self.root.mainloop()

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


    def nextB(self):
        self.databseConnection()
        self.mycursor=self.mydb.cursor()

        self.textbox.delete('1.0', tk.END)

        self.id = (self.questions[self.num],)
        self.sql="select question,answer1,answer2,answer3,answer4,correctAnswer from questions where qID=%s"

        self.mycursor.execute(self.sql,self.id)
        self.myt=self.mycursor.fetchone()
        self.y=f"{self.myt[0]} \nOption 1: {self.myt[1]} \nOption 2: {self.myt[2]} \nOption 3: {self.myt[3]} \nOption 4:{self.myt[4]}"
        self.textbox.insert(tk.END, self.y)
        self.correctanswers.append(self.myt[5])
        self.num = self.num - 1
        print(self.correctanswers)
        print(self.num)


        if self.num < 0:
            self.textbox.delete('1.0', tk.END)
            self.textbox.insert(tk.END, "Click Finish!!!!")
        #self.addb()


    #start
    def getQuestionList(self):
        while self.totalQuestions > 0:
            x = random.randrange(1, 25)
            if x in self.questions:
                continue
            else:
                self.questions.append(x)

            self.totalQuestions = self.totalQuestions - 1
        print(self.questions)
        self.textbox.delete('1.0', tk.END)
        self.textbox.insert(tk.END, "Click Next Button")
        self.start["state"]=tk.DISABLED
        return self.questions

    def addb(self):
        self.val=self.v.get()
        if self.num>=0:
            self.answers.append(self.val)
            print(self.answers)
            self.textbox.insert(tk.END, "Click Next Button")
        else:
            tkinter.messagebox.showinfo("","Your attempts are over")
        self.textbox.delete('1.0', tk.END)

#finish
    def getTotalMark(self):
        y=len(self.answers)-1
        while y>= 0:
            if self.answers[y] == self.correctanswers[y]:
                self.marks = self.marks + 1
            y=y-1


        try:
            self.databseConnection()
            self.mycursor=self.mydb.cursor()
            self.userId=int(self.e1.get())
            self.sql2="insert into marks(userID,marks) values(%s,%s)"
            self.val = (self.userId, self.marks)
            self.mycursor.execute(self.sql2, self.val)
            self.mydb.commit()

        except:
            tkinter.messagebox.showinfo("Message", f'Invalid User ID')



        self.b5["state"]=tk.DISABLED
        tkinter.messagebox.showinfo("Message",f'Your Total mark = {self.marks}/10')

#show question window with correct answers
    def root2(self):
        self.root.destroy()
        self.num = 9
        self.root = tk.Tk()
        self.root.geometry("550x300")
        self.root.title("Correct Answers")
        self.f2 = tk.Frame(self.root, bg='green')
        self.f2.place(x=0, y=0, width=550, height=300)
        self.textbox = tk.Text(self.f2, height="10", width="80")
        self.textbox_value = tk.StringVar()
        self.textbox.pack()


        self.next = tk.Button(self.f2, text="Next", bg="blue", command=self.click)
        self.next.place(x=250, y=200, width=100, height=50)

        self.textbox.insert(tk.END, "Click Next to see correct answers")

#next button to get quetsion with correct answers
    def click(self):
        self.databseConnection()
        self.mycursor = self.mydb.cursor()

        self.textbox.delete('1.0', tk.END)
        print(self.questions)

        self.id = (self.questions[self.num],)
        self.sql = "select question,answer1,answer2,answer3,answer4,correctAnswer from questions where qID=%s"

        self.mycursor.execute(self.sql, self.id)
        self.myt = self.mycursor.fetchone()
        self.y = f"{self.myt[0]} \nOption 1: {self.myt[1]} \nOption 2: {self.myt[2]} \nOption 3: {self.myt[3]} \nOption 4:{self.myt[4]}\n Correct Answer : {self.myt[5]}"
        self.textbox.insert(tk.END, self.y)
        self.num = self.num - 1
        print(self.num)

        if self.num==-1:
            self.next["state"]=tk.DISABLED



#q1=questionwindow()


