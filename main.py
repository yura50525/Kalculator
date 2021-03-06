from tkinter import *

def dob():
  rez = float(enter1.get())*float(enter2.get())
  enter3.delete(0,END)
  enter3.insert(0,rez)

def riz():
  rez = float(enter1.get())-float(enter2.get())
  enter3.delete(0,END)
  enter3.insert(0,rez)

def sym():
  rez = float(enter1.get())+float(enter2.get())
  enter3.delete(0,END)
  enter3.insert(0,rez)

def cha():
  rez = float(enter1.get())/float(enter2.get())
  enter3.delete(0,END)
  enter3.insert(0,rez)


root = Tk()
root.title("Калькулятор")
root.geometry("300x300")
root.maxsize(300, 300)

l = Label(root, text="Введіть 1 число")
l2 = Label(root, text="Введіть 2 число")
l3 = Label(root, text="Результат:")
l.pack()


enter1 = Entry(root)
enter1.pack()
l2.pack()

enter2 = Entry(root)
enter2.pack()

but = Button(text = "+", command=sym)
but.place(x=60,y=90)

but = Button(text = "-", command=riz)
but.place(x=110,y=90)

but = Button(text = "*", command=dob)
but.place(x=150,y=90)

but = Button(text = "/", command=cha)
but.place(x=200,y=90)
l3.place(x=110,y=120)

enter3 = Entry()
enter3.place(x=63,y=140)

root.mainloop()


