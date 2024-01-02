# Text writing
from tkinter import *
from tkinter import ttk

text = Tk()
text.title("🤷‍♂️😜😎TextWriting😍👍👌(●'◡'●)(❁´◡`❁)")
text.geometry('400x500')
text.config(bg="blue")


# comb_sor = ttk.Combobox(text,values=type)

lab = Label(text="TypingPractice",font=('Time New Roman',20,"bold"),bg="red",fg="white")
lab.place(x=50,y=20,height=35,width=300)

lab_txt=Text(text,font=('Time New Roman',40,"bold"),bg='yellow',fg="orange",border=30,borderwidth=45)
lab_txt.place(x=50,y=80,height=400,width=300)


# text()
text.mainloop()
# Tk()