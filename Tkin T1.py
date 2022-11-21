from tkinter import *
D = Tk()
D.geometry("340x450")
D.title("CALCULATOR")
Dlabel = Label(D, text="CALCULATOR", font =("Courier New",24,'bold'))
Dlabel.pack(side=TOP)

textin = StringVar()
operator=""

def clickbut(numbers):
    global operator
    operator=operator+str(numbers)
    textin.set(operator)

def equlbut():
    global operator
    add=str(eval(operator))
    textin.set(add)
    operator=' '

def equlbut():
    global operator
    sub=str(eval(operator))
    textin.set(sub)
    operator=' '

def equlbut():
    global operator
    mul=str(eval(operator))
    textin.set(mul)
    operator=' '

def equlbut():
    global operator
    div=str(eval(operator))
    textin.set(div)
    operator=' '

def clrbut():
    textin.set('')

Dtext = Entry(D, font=("Courier New", 12, 'bold'), textvar=textin,width=25,bd=5,bg='powder blue')
Dtext.pack()

but1= Button(D, padx=10, pady=10,bd=4,bg='light blue',command=lambda:clickbut(1),text="1",font=("Courier New",12,'bold'))
but1.place(x =10,y=100)

but2= Button(D, padx=10, pady=10,bd=4,bg='light blue',command=lambda:clickbut(2),text="2",font=("Courier New",12,'bold'))
but2.place(x=70,y=100)

but3= Button(D, padx=10, pady=10,bd=4,bg='light blue',command=lambda:clickbut(3),text="3",font=("Courier New",12,'bold'))
but3.place(x=130,y=100)

but4= Button(D, padx=10, pady=10,bd=4,bg='light blue',command=lambda:clickbut(4),text="4",font=("Courier New",12,'bold'))
but4.place(x=10,y=170)

but5= Button(D, padx=10, pady=10,bd=4,bg='light blue',command=lambda:clickbut(5),text="5",font=("Courier New",12,'bold'))
but5.place(x=70,y=170)

but6= Button(D, padx=10, pady=10,bd=4,bg='light blue',command=lambda:clickbut(6),text="6",font=("Courier New",12,'bold'))
but6.place(x=130,y=170)

but7= Button(D, padx=10, pady=10,bd=4,bg='light blue',command=lambda:clickbut(7),text="7",font=("Courier New",12,'bold'))
but7.place(x=10,y=240)

but8= Button(D, padx=10, pady=10,bd=4,bg='light blue',command=lambda:clickbut(8),text="8",font=("Courier New",12,'bold'))
but8.place(x=70,y=240)

but9= Button(D, padx=10, pady=10,bd=4,bg='light blue',command=lambda:clickbut(9),text="9",font=("Courier New",12,'bold'))
but9.place(x=130,y=240)

butz= Button(D, padx=10, pady=10,bd=4,bg='light blue',command=lambda:clickbut(0),text="0",font=("Courier New",12,'bold'))
butz.place(x=10,y=310)

butsp= Button(D, padx=40, pady=10,bd=4,bg='light blue',command=lambda:clickbut(" "),text=".",font=("Courier New",12,'bold'))
butsp.place(x=70,y=310)

butpl= Button(D, padx=10, pady=10,bd=4,bg='light blue',command=lambda:clickbut("+"),text="+",font=("Courier New",12,'bold'))
butpl.place(x=190,y=100)

butsub= Button(D, padx=10, pady=10,bd=4,bg='light blue',command=lambda:clickbut("-"),text="-",font=("Courier New",12,'bold'))
butsub.place(x=190,y=170)

butmul= Button(D, padx=10, pady=10,bd=4,bg='light blue',command=lambda:clickbut("*"),text="*",font=("Courier New",12,'bold'))
butmul.place(x=190,y=240)

butdiv= Button(D, padx=10, pady=10,bd=4,bg='light blue',command=lambda:clickbut("/"),text="/",font=("Courier New",12,'bold'))
butdiv.place(x=190,y=310)

buteq= Button(D, padx=100, pady=10,bd=4,bg='light blue',command=equlbut,text="=",font=("Courier New",12,'bold'))
buteq.place(x=10,y=380)

butclr= Button(D, padx=10, pady=150,bd=4,bg='light blue',command=clrbut,text="Clr",font=("Courier New",12,'bold'))
butclr.place(x=250,y=100)

D.mainloop()
