from tkinter import *
import math
import pyperclip



RELWIDTH=0.141
RELHEIGHT=0.19
GAP = 0.01
BG = 'blue'
FG = 'orange'
mode=FALSE
CNF_BUTTON = {
    'bg': BG,
    'fg': FG,
    'font' : ('',24),
}

def clear():
    entry.delete(0,END)
def copy():
    pyperclip.copy(entry.get())
def clear1():
    length = len(entry.get())
    entry.delete(length-1,END)

def my_abs():
    global mode

    temp = entry.get()
    clear()
   
    try:
        temp= eval(temp)
        if mode:
            result=(math.sin(math.radians(temp)))
        else:
            result = abs(temp)
        
        entry.insert(0, result)
    except:
        entry.insert(0, 'ERROR')


def reverse():
    global mode
    temp = entry.get()
    clear()
    try:
        temp= eval(temp)
        if mode:
            result=(math.cos(math.radians(temp)))
        else:
            result = 1/temp
        entry.insert(0, result)
    except:
        entry.insert(0, 'ERROR')

def sqrt():
    global mode
    temp = entry.get()
    clear()
    try:
        temp= eval(temp)
        if mode:
           result = math.tan(math.radians(temp))
        else:
             result = math.sqrt(temp)
        entry.insert(0, result)
    except:
        entry.insert(0, 'ERROR')
def x2():
    temp = entry.get()
    clear()
    try:
        temp= eval(temp)
        if mode:
           result = math.log(temp)
        else:
             result = math.x2(temp)
        entry.insert(0, result)
    except:
        entry.insert(0, 'ERROR')
def equal():
    temp = entry.get()
    entry.delete(0, END)
    try:
        temp = eval(temp)
        entry.insert(0, str(temp))
    except SyntaxError:
        entry.insert(0, 'ERROR')
    except ZeroDivisionError:
        entry.insert(0, 'ERROR')

def insert(character):
    entry.insert(END, character)

def seconde():
    global mode
    mode= not mode
    if mode:
        btn_abs_sin.config(text='sin(x)')
        btn_reverse_cos.config(text='cos(x)')
        btn_sqrt_tang.config(text='tang(x)')
        btn_x2_log.config(text='log(x)')
    else:
        btn_abs_sin.config(text='|x|')
        btn_reverse_cos.config(text='1/x')
        btn_sqrt_tang.config(text='√x')
        btn_x2_log.config(text='x2')


root= Tk()
root.geometry('1000x500')
root.minsize(700,400)
root.config(bg=BG)
entry = Entry(root,font=('', 24) )
entry                   .place(relx=GAP,                                 rely=RELHEIGHT*0+GAP, relwidth=RELWIDTH*6, relheight=RELHEIGHT )
Button(root,text='copy',cnf = CNF_BUTTON, command=copy).place(relx=RELWIDTH*6+GAP           ,rely=RELHEIGHT*0+GAP, relwidth=RELWIDTH*1, relheight=RELHEIGHT)
btn_abs_sin = Button(root,text='|x|',cnf = CNF_BUTTON, command= my_abs)
btn_abs_sin.place(relx=0+GAP                  ,rely=RELHEIGHT*1+GAP, relwidth=RELWIDTH*1, relheight=RELHEIGHT)
btn_reverse_cos=Button(root,text='1/X',cnf = CNF_BUTTON, command=reverse)
btn_reverse_cos.place(relx=RELWIDTH*1+GAP         ,rely=RELHEIGHT*1+GAP, relwidth=RELWIDTH*1, relheight=RELHEIGHT)
btn_sqrt_tang=Button(root,text='√X',cnf = CNF_BUTTON, command=sqrt)
btn_sqrt_tang.place(relx=RELWIDTH*2+GAP             ,rely=RELHEIGHT*1+GAP, relwidth=RELWIDTH*1, relheight=RELHEIGHT)
btn_x2_log=Button(root,text='x²',cnf = CNF_BUTTON, command=x2)
btn_x2_log.place(relx=RELWIDTH*3+GAP               ,rely=RELHEIGHT*1+GAP, relwidth=RELWIDTH*1, relheight=RELHEIGHT)
Button(root,text='2nd',cnf = CNF_BUTTON, command= seconde).place(relx=RELWIDTH*4+GAP,rely=RELHEIGHT*1+GAP     ,relwidth=RELWIDTH*1, relheight=RELHEIGHT)
Button(root,text='*',cnf = CNF_BUTTON,command=lambda:insert('*')).place(relx=RELWIDTH*5+GAP ,rely=RELHEIGHT*1+GAP, relwidth=RELWIDTH*1, relheight=RELHEIGHT)
Button(root,text='←',cnf = CNF_BUTTON, command=clear1).place(relx=RELWIDTH*6+GAP            ,rely=RELHEIGHT*1+GAP, relwidth=RELWIDTH*1, relheight=RELHEIGHT)
for i in range(1,6):
    Button(root,text=i, cnf = CNF_BUTTON, command=lambda i=i:insert(i)).place(relx=RELWIDTH*(i-1)+GAP     ,  rely=RELHEIGHT*1.9+GAP*3, relwidth=RELWIDTH*1, relheight=RELHEIGHT)
Button(root,text='/',cnf = CNF_BUTTON,command=lambda:insert('/')).place(relx=RELWIDTH*5+GAP,               rely=RELHEIGHT*1.9+GAP*3, relwidth=RELWIDTH*1, relheight=RELHEIGHT)
Button(root,text='clear',cnf = CNF_BUTTON,command=clear).place(relx=RELWIDTH*6+GAP,               rely=RELHEIGHT*1.9+GAP*3, relwidth=RELWIDTH*1, relheight=RELHEIGHT)
Button(root,text='0',cnf = CNF_BUTTON, command=lambda:insert('0')).place(relx=RELWIDTH*4+GAP,               rely=RELHEIGHT*3+GAP*2, relwidth=RELWIDTH*1, relheight=RELHEIGHT)
Button(root,text='-',cnf = CNF_BUTTON,command=lambda:insert('-')).place(relx=RELWIDTH*5+GAP,               rely=RELHEIGHT*3+GAP*2, relwidth=RELWIDTH*1, relheight=RELHEIGHT)
Button(root,text='+',cnf = CNF_BUTTON,command=lambda:insert('+')).place(relx=RELWIDTH*6+GAP,               rely=RELHEIGHT*3+GAP*2, relwidth=RELWIDTH*1, relheight=RELHEIGHT*2)
for i in range(6,10):
    Button(root,text=i, cnf = CNF_BUTTON, command=lambda i=i:insert(i)).place(relx=RELWIDTH*(i-6)+GAP     ,  rely=RELHEIGHT*2.9+GAP*4, relwidth=RELWIDTH*1, relheight=RELHEIGHT)
Button(root,text='000',cnf = CNF_BUTTON,command=lambda:insert('000'))    .place(relx=RELWIDTH*0+GAP      ,rely=RELHEIGHT*4+GAP*2.2, relwidth=RELWIDTH*2, relheight=RELHEIGHT)
Button(root,text='.',cnf = CNF_BUTTON,command=lambda:insert('.'))      .place(relx=RELWIDTH*2+GAP      ,rely=RELHEIGHT*4+GAP*2.2, relwidth=RELWIDTH*1, relheight=RELHEIGHT)
Button(root,text='(',cnf = CNF_BUTTON,command=lambda:insert('('))      .place(relx=RELWIDTH*3+GAP      ,rely=RELHEIGHT*4+GAP*2.2, relwidth=RELWIDTH*1, relheight=RELHEIGHT)
Button(root,text=')',cnf = CNF_BUTTON,command=lambda:insert(')'))      .place(relx=RELWIDTH*4+GAP      ,rely=RELHEIGHT*4+GAP*2.2, relwidth=RELWIDTH*1, relheight=RELHEIGHT)
Button(root,text='=',bg= 'green', fg='white', activebackground='lime',activeforeground='white',cnf = CNF_BUTTON, command=equal)      .place(relx=RELWIDTH*5+GAP      ,rely=RELHEIGHT*4+GAP*2.2, relwidth=RELWIDTH*1, relheight=RELHEIGHT)


root.mainloop()