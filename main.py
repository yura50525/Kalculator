from tkinter import *

#Functions
def B_1():
    ent.insert(END,"1")

def B_2():
    ent.insert(END,"2")

def B_3():
    ent.insert(END,"3")

def B_4():
    ent.insert(END,"4")

def B_5():
    ent.insert(END,"5")

def B_6():
    ent.insert(END,"6")

def B_7():
    ent.insert(END,"7")

def B_8():
    ent.insert(END,"8")

def B_9():
    ent.insert(END,"9")

root = Tk()
root.geometry("260x370")
root.title("Калькулятор ")

ent=Entry(justify="right", font="arial,14")
ent.place(x=20,y=20,width=220,height=30)
#1 colon
B1=Button(text="1",font="14",command=B_1)
B1.place(x=20,y=230,width=40,height=40)

B2=Button(text="2",font="14",command=B_2)
B2.place(x=80,y=230,width=40,height=40)

B3=Button(text="3",font="14",command=B_3)
B3.place(x=140,y=230,width=40,height=40)

#2 colon
B4=Button(text="4",font="14",command=B_4)
B4.place(x=20,y=180,width=40,height=40)

B5=Button(text="5",font="14",command=B_5)
B5.place(x=80,y=180,width=40,height=40)

B6=Button(text="6",font="14",command=B_6)
B6.place(x=140,y=180,width=40,height=40)

#3 ряд
B7=Button(text="7",font="14",command=B_7)
B7.place(x=20,y=130,width=40,height=40)

B8=Button(text="8",font="14",command=B_8)
B8.place(x=80,y=130,width=40,height=40)

B9=Button(text="9",font="14",command=B_9)
B9.place(x=140,y=130,width=40,height=40)

#actions

but1 = Button(text = "+")#, command=)
but1.place(x=20,y=290,width=40,height=40)

but2 = Button(text = "-")#, command=)
but2.place(x=80,y=290,width=40,height=40)

but3 = Button(text = "*")#, command=)
but3.place(x=140,y=290,width=40,height=40)

but4 = Button(text = "/")#, command=)
but4.place(x=200,y=290,width=40,height=40)


root.mainloop()
