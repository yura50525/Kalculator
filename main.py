from tkinter import *
from math import sqrt

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

def B_0():
    ent.insert(END,"0")

def B_P():
    ent.insert(END,".")

def dela():
    ent.delete(0,END)

def dele():
    ent.delete(0)

def p():
    global a,b
    a=float(ent.get())
    b="+"
    ent.delete(0,END)

def m():
    global a1,b
    a1=float(ent.get())
    b="*"
    ent.delete(0,END)

def min():
    global a2,b
    a2=float(ent.get())
    b="-"
    ent.delete(0,END)

def d():
    global a3,b
    a3=float(ent.get())
    b="/"
    ent.delete(0,END)

def step():
    global a5,b
    a5=int(ent.get())
    b="^"
    ent.delete(0,END)

def kor():
    global a4,b,a44
    a4=float(ent.get())
    a44= sqrt(a4)
    b="√"
    ent.delete(0,END)
    ent.insert(END,a44)

def rez():
    global a1,b,a2,a3,a5
    if b=="+":
      c=float(ent.get())+a
      ent.delete(0,END)
      ent.insert(END,str(c))
    elif b=="*":
      c=float(ent.get())*a1
      ent.delete(0,END)
      ent.insert(END,str(c))
    elif b=="-":
      c=a2 - float(ent.get())
      ent.delete(0,END)
      ent.insert(END,str(c))
    elif b=="/":
      c=a3 / float(ent.get())
      ent.delete(0,END)
      ent.insert(END,str(c))
    elif b=="^":
      c=a5 ** int(ent.get())
      ent.delete(0,END)
      ent.insert(END,str(c))



root = Tk()
root.geometry("260x370")
root.title("Калькулятор ")
root.config(bg = "white")

ent=Entry(justify="right", font="arial,14",border=2)
ent.place(x=20,y=20,width=220,height=30)
#1 colon
B1=Button(text="1",font="14",command=B_1,border=0,bg = "white")
B1.place(x=20,y=230,width=40,height=40)

B2=Button(text="2",font="14",command=B_2,border=0,bg = "white")
B2.place(x=80,y=230,width=40,height=40)

B3=Button(text="3",font="14",command=B_3,border=0,bg = "white")
B3.place(x=140,y=230,width=40,height=40)

#2 colon
B4=Button(text="4",font="14",command=B_4,border=0,bg = "white")
B4.place(x=20,y=180,width=40,height=40)

B5=Button(text="5",font="14",command=B_5,border=0,bg = "white")
B5.place(x=80,y=180,width=40,height=40)

B6=Button(text="6",font="14",command=B_6,border=0,bg = "white")
B6.place(x=140,y=180,width=40,height=40)

#3 ряд
B7=Button(text="7",font="14",command=B_7,border=0,bg = "white")
B7.place(x=20,y=130,width=40,height=40)

B8=Button(text="8",font="14",command=B_8,border=0,bg = "white")
B8.place(x=80,y=130,width=40,height=40)

B9=Button(text="9",font="14",command=B_9,border=0,bg = "white")
B9.place(x=140,y=130,width=40,height=40)

B0=Button(text="0",font="14",command=B_0,border=0,bg = "white")
B0.place(x=80,y=290,width=40,height=40)

Bp=Button(text=".",font="14",command=B_P,border=0,bg = "white")
Bp.place(x=140,y=290,width=40,height=40)

#actions



but1 = Button(text = "+", command=p,border=0,bg = "white",fg="#F89414")
but1.place(x=200,y=230,width=40,height=40)

but2 = Button(text = "÷", command=d,border=0,bg = "white",fg="#F89414")
but2.place(x=200,y=70,width=40,height=40)

but3 = Button(text = "×", command=m,border=0,bg = "white",fg="#F89414")
but3.place(x=200,y=130,width=40,height=40)

but4 = Button(text = "-", command=min,border=0,bg = "white",fg="#F89414")
but4.place(x=200,y=180,width=40,height=40)

but5 = Button(text = "=", command=rez,bg="#F89414",fg="white",border=0)
but5.place(x=200,y=290,width=40,height=40)


but6 = Button(text = "√", command=kor,border=0,bg = "white",fg="#F89414")
but6.place(x=140,y=70,width=40,height=40)

but7 = Button(text = "x^y", command=step,border=0,bg = "white")
but7.place(x=20,y=290,width=40,height=40)

but8 = Button(text = "AC", command=dela,border=0,bg = "white",fg="#F89414")
but8.place(x=20,y=70,width=40,height=40)

but9 = Button(text = "С", command=dele,border=0,bg = "white",fg="#F89414")
but9.place(x=80,y=70,width=40,height=40)


root.mainloop()
