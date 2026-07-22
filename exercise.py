# from tkinter import *
# import math



# RELWIDTH = 0.14
# RELHEIGHT = 0.2
# CNF_BUTTON = {    
#     "bg" :  'skyblue',
#     "fg" :  'white',
#    "font": '24',
# }


# GAP=0.01

# def insert(charactor):
#     entry.insert('end',charactor)

# def equal():
#     temp = entry.get()
#     entry.delete(0,END)
#     print(temp)
#     try:
#         temp = eval(temp)
#         entry.insert(0,temp)
#     except SyntaxError:
#         entry.insert(0,"ERORR")
#     except ZeroDivisionError:
#         entry.insert(0,"ERROR")
#     except TypeError:
#         entry.insert(0,"ERROR")
#     except NameError:
#         entry.insert(0,"ERROR")

# def clear():
#     entry.delete(0,END)



# def clear1():
#     length= len(entry.get())
#     entry.delete(length-1,END)

# def reverse():
#     temp = entry.get()
#     entry.delete(0,END)
#     try:
#         temp= eval(temp)
#         result = 1/temp
#         entry.insert(0, result)
#     except:
#         entry.insert(0,"ERROR")

# def my_abs():
#     temp = entry.get()
#     entry.delete(0,END)
#     try:
#         temp= eval(temp)
#         result = abs(temp)
#         entry.insert(0, result)
#     except:
#         entry.insert(0,"ERROR")

# def sqrt():
#     temp = entry.get()
#     entry.delete(0,END)
#     try:
#         temp= eval(temp)
#         result = math.sqrt(temp)
#         entry.insert(0, result)
#     except:
#         entry.insert(0,"ERROR")


# def x2():
#     temp = entry.get()
#     entry.delete(0,END)
#     try:
#         temp= eval(temp)
#         result = temp**2
#         entry.insert(0, result)
#     except:
#         entry.insert(0,"ERROR")








# root=Tk()
# root.title("CALCULATOR")
# root.geometry("1000x700")
# root.config(bg = "sky blue")
# entry = Entry(root, text="", font=("", 24))
# entry.place(relx= 0+GAP,rely=0+GAP, relwidth=RELWIDTH*6, relheight = RELHEIGHT)
# Button(root,text="copy", cnf = CNF_BUTTON)   .place(relx=RELWIDTH*6+GAP     ,rely=0+GAP, relwidth=RELWIDTH, relheight= RELHEIGHT)
# Button(root,text="|x|", cnf = CNF_BUTTON, command=my_abs)    .place(relx=RELWIDTH*0+GAP     ,rely=RELHEIGHT*1+GAP       ,relwidth=RELWIDTH      ,relheight= RELHEIGHT)
# Button(root,text="1/x", cnf = CNF_BUTTON, command =reverse)    .place(relx=RELWIDTH*1+GAP     ,rely=RELHEIGHT*1+GAP       ,relwidth=RELWIDTH      ,relheight= RELHEIGHT)
# Button(root,text="√x", cnf = CNF_BUTTON, command=sqrt)     .place(relx=RELWIDTH*2+GAP     ,rely=RELHEIGHT*1+GAP       ,relwidth=RELWIDTH      ,relheight= RELHEIGHT)
# Button(root,text="x2", cnf = CNF_BUTTON, command=x2)     .place(relx=RELWIDTH*3+GAP     ,rely=RELHEIGHT*1+GAP       ,relwidth=RELWIDTH      ,relheight= RELHEIGHT)
# Button(root,text="second", cnf = CNF_BUTTON) .place(relx=RELWIDTH*4+GAP     ,rely=RELHEIGHT*1+GAP       ,relwidth=RELWIDTH      ,relheight= RELHEIGHT)



# for i in range(1,6):
#     Button(root, text=i, cnf=CNF_BUTTON, command=lambda i=i:insert(i))      .place(relx=(i-1)*RELWIDTH+GAP ,  rely=RELHEIGHT*2+GAP,relwidth= RELWIDTH, relheight=RELHEIGHT)


# for i in range(6,10):
#     Button(root, text=i, cnf=CNF_BUTTON, command=lambda i=i:insert(i))      .place(relx=(i-6)*RELWIDTH+GAP ,  rely=RELHEIGHT*3+GAP,relwidth= RELWIDTH, relheight=RELHEIGHT)




# Button(root,text="0", cnf = CNF_BUTTON, command=lambda:insert("0"))             .place(relx=RELWIDTH*4+GAP          , rely=RELHEIGHT*3+GAP      , relwidth=RELWIDTH         ,relheight= RELHEIGHT)
# Button(root, text="000", cnf=CNF_BUTTON, command=lambda:insert("000"))            .place(relx=RELWIDTH*0+GAP          , rely=RELHEIGHT*4+GAP      , relwidth=RELWIDTH*2       ,relheight=RELHEIGHT)
# Button(root, text=".", cnf=CNF_BUTTON, command=lambda:insert("."))              .place(relx=RELWIDTH*2+GAP          , rely=RELHEIGHT*4+GAP      , relwidth=RELWIDTH         ,relheight=RELHEIGHT)
# Button(root, text="(", cnf=CNF_BUTTON, command=lambda:insert("("))              .place(relx=RELWIDTH*3+GAP          , rely=RELHEIGHT*4+GAP      , relwidth=RELWIDTH         ,relheight=RELHEIGHT)
# Button(root, text=")", cnf=CNF_BUTTON, command=lambda:insert(")"))              .place(relx=RELWIDTH*4+GAP          , rely=RELHEIGHT*4+GAP      , relwidth=RELWIDTH         ,relheight=RELHEIGHT)
# Button(root, text="=", cnf=CNF_BUTTON, fg="black", bg="green", command =equal)              .place(relx=RELWIDTH*5+GAP          , rely=RELHEIGHT*4+GAP      , relwidth=RELWIDTH         ,relheight=RELHEIGHT)
# Button(root, text="+", cnf=CNF_BUTTON, command=lambda:insert("+"))              .place(relx=RELWIDTH*6+GAP          , rely=RELHEIGHT*3+GAP      , relwidth=RELWIDTH         ,relheight=RELHEIGHT*2)
# Button(root, text="/", cnf=CNF_BUTTON, command=lambda:insert("/"))              .place(relx=RELWIDTH*5+GAP          , rely=RELHEIGHT*2+GAP      , relwidth=RELWIDTH         ,relheight=RELHEIGHT)
# Button(root,text="clear", cnf = CNF_BUTTON, command=clear)         .place(relx=RELWIDTH*6+GAP          , rely=RELHEIGHT*2+GAP      , relwidth=RELWIDTH         ,relheight= RELHEIGHT)
# Button(root,text="-", cnf = CNF_BUTTON, command=lambda:insert("-"))             .place(relx=RELWIDTH*5+GAP          , rely=RELHEIGHT*3+GAP      , relwidth=RELWIDTH         ,relheight= RELHEIGHT)
# Button(root,text="*", cnf = CNF_BUTTON, command=lambda:insert("*"))      .place(relx=RELWIDTH*5+GAP     ,rely=RELHEIGHT*1+GAP       ,relwidth=RELWIDTH      ,relheight= RELHEIGHT)
# Button(root,text="←", cnf = CNF_BUTTON, command = clear1)      .place(relx=RELWIDTH*6+GAP     ,rely=RELHEIGHT*1+GAP       ,relwidth=RELWIDTH      ,relheight= RELHEIGHT)
# root.mainloop()



# from tkinter import*



# root = Tk()


# CNF_BUTTON = {
#     'bg':'#333333',
#     'fg':'orange',
#     'font':('',48),
# }

# CNF_GRID = {
#     'padx':5,
#     'pady':5
# }

# btn1= Button(root,text="1",cnf=CNF_BUTTON)
# btn2= Button(root,text="2",cnf=CNF_BUTTON)
# btn3= Button(root,text="3",cnf=CNF_BUTTON)
# btn4= Button(root,text="4",cnf=CNF_BUTTON)
# btn5= Button(root,text="5",cnf=CNF_BUTTON)
# btn6= Button(root,text="6",cnf=CNF_BUTTON)
# btn7= Button(root,text="7",cnf=CNF_BUTTON)
# btn8= Button(root,text="8",cnf=CNF_BUTTON)
# btn9= Button(root,text="9",cnf=CNF_BUTTON)
# btn10= Button(root,text="10",cnf=CNF_BUTTON)


# btn1.grid(row=1,column=1, cnf=CNF_GRID)
# btn2.grid(row=1,column=2, cnf=CNF_GRID)
# btn3.grid(row=2,column=1, cnf=CNF_GRID)
# btn4.grid(row=2,column=2, cnf=CNF_GRID)
# btn5.grid(row=1,column=3, cnf=CNF_GRID, rowspan=2   , sticky='ns')
# btn6.grid(row=3,column=1, cnf=CNF_GRID, columnspan=3, sticky='ew')
# btn7.grid(row=1,column=4, cnf=CNF_GRID)
# btn8.grid(row=2,column=4, cnf=CNF_GRID, rowspan=2, sticky='ns')
# btn9.grid(row=4,column=1, cnf=CNF_GRID, columnspan=4, sticky='ew')
# btn10.grid(row=1,column=5, cnf=CNF_GRID, rowspan=3, sticky='ns')


# root.mainloop()





from tkinter import*

root=Tk()

CNF_BUTTON = {
    'bg' :'skyblue',
    'fg' : 'white',
    'font' : ('',48)
}


CNF_GRID ={
    'padx':'5',
    'pady':'5',
}
root.geometry("1000x800")
btn1= Button(root,text="1",cnf=CNF_BUTTON)
btn2= Button(root,text="2",cnf=CNF_BUTTON, anchor='nw')
btn3= Button(root,text="3",cnf=CNF_BUTTON,width=5)
btn4= Button(root,text="4",cnf=CNF_BUTTON)
btn5= Button(root,text="5",cnf=CNF_BUTTON)
btn6= Button(root,text="6",cnf=CNF_BUTTON,width=5)
btn7= Button(root,text="7",cnf=CNF_BUTTON)
btn8= Button(root,text="8",cnf=CNF_BUTTON)
btn9= Button(root,text="9",cnf=CNF_BUTTON)
btn10= Button(root,text="10",cnf=CNF_BUTTON)

btn1.grid(row=1,column=1 , cnf=CNF_GRID)
btn2.grid(row=1,column=2 , cnf=CNF_GRID, rowspan=2, columnspan=2, sticky='nsew')
btn4.grid(row=2,column=1 , cnf=CNF_GRID)
btn8.grid(row=3,column=1 , cnf=CNF_GRID)
btn5.grid(row=3,column=2 , cnf=CNF_GRID)
btn9.grid(row=3,column=3 , cnf=CNF_GRID)
btn3.grid(row=1,column=4 , cnf=CNF_GRID,columnspan=2, sticky='ew')
btn6.grid(row=2,column=4 , cnf=CNF_GRID, rowspan=2, columnspan=4, sticky='nsew')
btn7.grid(row=4,column=1 , cnf=CNF_GRID, columnspan=6, sticky='ew')




root.mainloop()




















































