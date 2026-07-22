# from tkinter import *
# from tkinter import messagebox
# def Save():
#     name=entry_name.get().strip()
#     surname= entry_surname.get()
#     number=entry_number.get()
#     print(name,surname,number)
#     if name=="":
#         messagebox.showerror("!", "This box can not empty!")
#         return
#     with open(name,"w") as f:
#         r=messagebox.askyesnocancel('Sure?','Are you sure you want to save info?')
#         if r==True:
#             f.write(f'Name: {name}\nSurname: {surname}\nNumber: {number}')
    
#         elif r==False:
#             messagebox.showinfo("ok","This info is not save!")
#         elif r==None:
#             messagebox.showerror("!","I don't understand!")





# root=Tk()
# root.geometry("700x400")
# root.title("ثبت نام افراد")
# label_name= Label(root, text="Enter your name:" ,font=("", 14))
# label_name.place(x=0,y=10, width= 300, height=60)
# entry_name=Entry(root, font=('', 14))
# entry_name.place(x=400,y=30,width= 250, height=60)
# label_surname= Label(root, text="Enter your surname:" ,font=("", 14))
# label_surname.place(x=60,y=120)
# entry_surname=Entry(root, font=('', 14))
# entry_surname.place(x=400,y=110,width= 250, height=60)
# label_number= Label(root, text="Enter your namenumber:" ,font=("", 14))
# label_number.place(x=50,y=220)
# entry_number=Entry(root, font=('', 14))
# entry_number.place(x=400,y=200,width= 250, height=60)
# button= Button(text="Exit", command=exit)
# button.place(x=400, y=300,width= 250, height=60)
# button= Button(text="Save", command=Save)
# button.place(x=10, y=300,width= 250, height=60)

# mainloop()




# from tkinter import *
# from PIL import Image,ImageTk

# SIZE = 128
# root= Tk()
# root.geometry('1000x1500')

# img_pizza = Image.open('C:/Users/KMCC/Desktop/films/New folder/images3.jpg')
# img_humberger = Image.open('C:/Users/KMCC/Desktop/films/New folder/images4.jpg')
# img_pasta = Image.open('C:/Users/KMCC/Desktop/films/New folder/images.jpg')
# img_stramboli = Image.open('C:/Users/KMCC/Desktop/films/New folder/images7.jpg')
# img_lazania = Image.open('C:/Users/KMCC/Desktop/films/New folder/images5.jpg')
# img_coka = Image.open('C:/Users/KMCC/Desktop/films/New folder/images6.jpg')



# img_pizza =img_pizza.resize((SIZE,SIZE))
# img_humberger =img_humberger.resize((SIZE,SIZE))
# img_pasta =img_pasta.resize((SIZE,SIZE))
# img_stramboli =img_stramboli.resize((SIZE,SIZE))
# img_lazania =img_lazania.resize((SIZE,SIZE))
# img_coka =img_coka.resize((SIZE,SIZE))

# img_pizza = ImageTk.PhotoImage(img_pizza)
# img_humberger = ImageTk.PhotoImage(img_humberger)
# img_pasta = ImageTk.PhotoImage(img_pasta)
# img_stramboli = ImageTk.PhotoImage(img_stramboli)
# img_lazania = ImageTk.PhotoImage(img_lazania)
# img_coka = ImageTk.PhotoImage(img_coka)


# button_pizza =Button(root , image=img_pizza)
# button_pizza.place(x=200,y=10+SIZE*0,width=SIZE,height=SIZE)

# button_humberger =Button(root , image=img_humberger)
# button_humberger.place(x=200,y=10*2+SIZE*1,width=SIZE,height=SIZE)

# button_pasta =Button(root , image=img_pasta)
# button_pasta.place(x=200,y=10*3+SIZE*2,width=SIZE,height=SIZE)


# button_stramboli =Button(root , image=img_stramboli)
# button_stramboli.place(x=200,y=10*4+SIZE*3,width=SIZE,height=SIZE)

# button_lazania =Button(root , image=img_lazania)
# button_lazania.place(x=200,y=10*5+SIZE*4,width=SIZE,height=SIZE)

# button_coka =Button(root , image=img_coka)
# button_coka.place(x=620,y=10+SIZE*0,width=SIZE,height=SIZE)

# button_pizza_minus = Button(root, text='-', font=('',20))
# button_pizza_minus.place(x=70,y=10, width=SIZE,height=SIZE)
# button_pizza_plus = Button(root, text='+', font=('',20))
# button_pizza_plus.place(x=200+SIZE+10,y=10+SIZE*0, width=SIZE,height=SIZE)

# button_humberger_minus = Button(root, text='-', font=('',20))
# button_humberger_minus.place(x=70,y=10*2+SIZE*1, width=SIZE,height=SIZE)
# button_humberger_plus = Button(root, text='+', font=('',20))
# button_humberger_plus.place(x=200+SIZE+10,y=10*2+SIZE*1, width=SIZE,height=SIZE)

# button_pasta_minus = Button(root, text='-', font=('',20))
# button_pasta_minus.place(x=70,y=10*3+SIZE*2, width=SIZE,height=SIZE)
# button_pasta_plus = Button(root, text='+', font=('',20))
# button_pasta_plus.place(x=200+SIZE+10,y=10*3+SIZE*2, width=SIZE,height=SIZE)

# button_stramboli_minus = Button(root, text='-', font=('',20))
# button_stramboli_minus.place(x=70,y=10*4+SIZE*3, width=SIZE,height=SIZE)
# button_stramboli_plus = Button(root, text='+', font=('',20))
# button_stramboli_plus.place(x=200+SIZE+10,y=10*4+SIZE*3, width=SIZE,height=SIZE)

# button_lazania_minus = Button(root, text='-', font=('',20))
# button_lazania_minus.place(x=70,y=10*5+SIZE*4, width=SIZE,height=SIZE)
# button_lazania_plus = Button(root, text='+', font=('',20))
# button_lazania_plus.place(x=200+SIZE+10,y=10*5+SIZE*4, width=SIZE,height=SIZE)


# button_coka_minus = Button(root, text='-', font=('',20))
# button_coka_minus.place(x=(200+SIZE+10)+150,y=10, width=SIZE,height=SIZE)
# button_coka_plus = Button(root, text='+', font=('',20))
# button_coka_plus.place(x=(200+SIZE+10)+420,y=10+SIZE*0, width=SIZE,height=SIZE)


# mainloop()



from tkinter import *
from PIL import Image,ImageTk
SIZE = 150


PRICE_PIZZA1 = 653000
PRICE_PIZZA2 = 550000
PRICE_PIZZA3 = 1200000
PRICE_PIZZA4 = 900000

PRICE_PASTA = 800000
PRICE_STRAMBOLI = 750000
PRICE_HAMBURGER = 900000
PRICE_FRIES = 300000

PRICE_SOUP = 110000
PRICE_COKE = 120000
PRICE_DOOGH = 100000
PRICE_DELESTER = 120000


BUTTON_CONFIG = {
    'activebackground': 'orange',
    'activeforeground':'#333333',
    'bg': '#333333',
    'fg': 'orange',
    'font': ('',28),
    'padx': 5,
    'pady':5
}
def change_window():
    window2.deiconify()
    root.withdraw()


root = Tk()
root.geometry('1000x1500')
root.config(bg="#333333")


img_pizza1  = Image.open(r'C:/Users/KMCC/Desktop/foods/image1.jpg')                   
img_pizza2  = Image.open(r'C:/Users/KMCC/Desktop/foods/image2.jpg')    
img_pizza3  = Image.open(r'C:/Users/KMCC/Desktop/foods/image3.jpg')   
img_pizza4  = Image.open(r'C:/Users/KMCC/Desktop/foods/image4.jpg')  



img_pizza1 = img_pizza1.resize((SIZE,SIZE))
img_pizza2 = img_pizza2.resize((SIZE,SIZE))
img_pizza3 = img_pizza3.resize((SIZE,SIZE))
img_pizza4 = img_pizza4.resize((SIZE,SIZE))


img_pizza1 = ImageTk.PhotoImage(img_pizza1)
img_pizza2 = ImageTk.PhotoImage(img_pizza2)
img_pizza3 = ImageTk.PhotoImage(img_pizza3)
img_pizza4 = ImageTk.PhotoImage(img_pizza4)



button_pizza1 = Button(root , image=img_pizza1, cnf = BUTTON_CONFIG)
button_pizza2 = Button(root , image=img_pizza2, cnf = BUTTON_CONFIG)
button_pizza3 = Button(root , image=img_pizza3, cnf = BUTTON_CONFIG)
button_pizza4 = Button(root , image=img_pizza4, cnf = BUTTON_CONFIG)



button_pizza1.place(x=50,y=10+SIZE*0,width=SIZE,height=SIZE )
button_pizza2.place(x=50,y=10*2+SIZE*1,width=SIZE,height=SIZE )
button_pizza3.place(x=50,y=10*3+SIZE*2,width=SIZE,height=SIZE )
button_pizza4.place(x=50,y=10*4+SIZE*3,width=SIZE,height=SIZE )


label_pizza1 =  Label(root, text=0, font=("Lora Italic",18) , cnf = BUTTON_CONFIG)

label_pizza2 =  Label(root, text=0, font=("Lora Italic",18) , cnf = BUTTON_CONFIG)

label_pizza3 =  Label(root, text=0, font=("Lora Italic",18) , cnf = BUTTON_CONFIG)

label_pizza4 =  Label(root, text=0, font=("Lora Italic",18) , cnf = BUTTON_CONFIG)


def calculate_total():

    total = 0

    total += int(label_pizza1['text']) * PRICE_PIZZA1
    total += int(label_pizza2['text']) * PRICE_PIZZA2
    total += int(label_pizza3['text']) * PRICE_PIZZA3
    total += int(label_pizza4['text']) * PRICE_PIZZA4

    total += int(label_pasta['text']) * PRICE_PASTA
    total += int(label_stramboli['text']) * PRICE_STRAMBOLI
    total += int(label_hamburger['text']) * PRICE_HAMBURGER
    total += int(label_frenchfries['text']) * PRICE_FRIES

    total += int(label_soup['text']) * PRICE_SOUP
    total += int(label_Coka['text']) * PRICE_COKE
    total += int(label_doogh['text']) * PRICE_DOOGH
    total += int(label_delester['text']) * PRICE_DELESTER

    total_label.config(text=f"جمع کل: {total:,} تومان")

def add(label, amount):
    temp = max(0, int(label['text']) + amount)
    label['text'] = temp
    calculate_total()

label_pizza1.place(x=280,y=18+SIZE*0)
label_pizza2.place(x=280,y=180+SIZE*0)
label_pizza3.place(x=280,y=340+SIZE*0)
label_pizza4.place(x=280,y=500+SIZE*0)




label1 = Label(root , text="پیتزا پپرونی",        font=("Lalezar",20) ,          cnf = BUTTON_CONFIG)
label2 = Label(root , text="653,000",        font=("Lalezar",16) ,                cnf = BUTTON_CONFIG)

label3 = Label(root , text= "پیتزا مرغ",          font=("Lalezar",20) ,          cnf = BUTTON_CONFIG)
label4 = Label(root , text= "550,000",          font=("Lalezar",16) ,             cnf = BUTTON_CONFIG)


label5= Label(root , text= "پیتزا گوشت و قارچ ", font=("Lalezar",20),            cnf = BUTTON_CONFIG)
label6 = Label(root , text= "1200,000", font=("Lalezar",16),                       cnf = BUTTON_CONFIG)


label7= Label(root , text="پیتزا مخصوص",          font=("Lalezar",20) ,          cnf = BUTTON_CONFIG)
label8= Label(root , text="900,000",          font=("Lalezar",16) ,          cnf = BUTTON_CONFIG)

label1.place(x=750,y=60+SIZE*0 )
label2.place(x=520,y=60+SIZE*0 )

label3.place(x=750,y=220+SIZE*0)
label4.place(x=520,y=220+SIZE*0 )

label5.place(x=700,y=380+SIZE*0)
label6.place(x=520,y=380+SIZE*0)


label7.place(x=730,y=540+SIZE*0)
label8.place(x=520,y=540+SIZE*0)



button_pizza1_minus = Button(root, text='-', font=('',18),command=lambda : add(label_pizza1, -1), cnf = BUTTON_CONFIG)

button_pizza1_plus = Button(root, text='+', font=('',18), command=lambda : add(label_pizza1, 1), cnf = BUTTON_CONFIG)

button_pizza2_minus = Button(root, text='-', font=('',18),command=lambda : add(label_pizza2, -1), cnf = BUTTON_CONFIG)

button_pizza2_plus = Button(root, text='+', font=('',18), command=lambda : add(label_pizza2, 1), cnf = BUTTON_CONFIG)

button_pizza3_minus = Button(root, text='-', font=('',18),command=lambda : add(label_pizza3, -1), cnf = BUTTON_CONFIG)

button_pizza3_plus = Button(root, text='+', font=('',18), command=lambda : add(label_pizza3, 1), cnf = BUTTON_CONFIG)

button_pizza4_minus = Button(root, text='-', font=('',18),command=lambda : add(label_pizza4, -1), cnf = BUTTON_CONFIG)

button_pizza4_plus = Button(root, text='+', font=('',18), command=lambda : add(label_pizza4, 1), cnf = BUTTON_CONFIG)


button_pizza1_minus.place(x=220,y=60)
button_pizza1_plus.place(x=330,y=60)
button_pizza2_minus.place(x=220,y=220)
button_pizza2_plus.place(x=330,y=220)
button_pizza3_minus.place(x=220,y=380)
button_pizza3_plus.place(x=330,y=380)
button_pizza4_minus.place(x=220,y=540)
button_pizza4_plus.place(x=330,y=540)



window2 = Toplevel(root)
window2.protocol("WM_DELETE_WINDOW",root.destroy)
window2.withdraw()
button_change = Button(root , text="صفحه بعد", font=("",18), command=lambda :change_window() ,cnf = BUTTON_CONFIG)
button_change.place(x=450,y=700)



window2.geometry('1000x1500')
SIZE=150
window2.config(bg="#333333")


total_label2 = Label(window2, text="جمع کل: 0", font=("Lalezar",22), cnf=BUTTON_CONFIG)
total_label2.place(x=400,y=900)



def change_window_to_3():
    window3.deiconify()
    window2.withdraw()

img_pasta = Image.open(r'C:/Users/KMCC/Desktop/foods/image5.jpg')   
img_stramboli = Image.open(r'C:/Users/KMCC\Desktop/foods/images.jpg')
img_hamburger = Image.open(r'C:/Users/KMCC/Desktop/foods/479-4798191_burger-and-fries-png-gourmet-burger-and-chips.jpg')
img_frenchfries = Image.open(r'C:/Users/KMCC/Desktop/foods/images7.jpg')





img_pasta =img_pasta.resize((SIZE,SIZE))
img_stramboli =img_stramboli.resize((SIZE,SIZE))
img_hamburger=img_hamburger.resize((SIZE,SIZE))
img_frenchfries=img_frenchfries.resize((SIZE,SIZE))




img_pasta = ImageTk.PhotoImage(img_pasta)
img_stramboli = ImageTk.PhotoImage(img_stramboli)
img_hamburger = ImageTk.PhotoImage(img_hamburger)
img_frenchfries = ImageTk.PhotoImage(img_frenchfries)






button_pasta = Button(window2 , image=img_pasta, cnf = BUTTON_CONFIG)
button_stramboli = Button(window2 , image=img_stramboli, cnf = BUTTON_CONFIG)
button_hamburger = Button(window2 , image=img_hamburger, cnf = BUTTON_CONFIG)
button_frenchfries = Button(window2 , image=img_frenchfries, cnf = BUTTON_CONFIG)





button_pasta.place(x=50,y=10+SIZE*0,width=SIZE,height=SIZE )
button_stramboli.place(x=50,y=10*2+SIZE*1,width=SIZE,height=SIZE )
button_hamburger.place(x=50,y=10*3+SIZE*2,width=SIZE,height=SIZE )
button_frenchfries.place(x=50,y=10*4+SIZE*3,width=SIZE,height=SIZE )





label_pasta =  Label(window2, text=0, font=("Lora Italic",18) , cnf = BUTTON_CONFIG)

label_stramboli =  Label(window2, text=0, font=("Lora Italic",18) , cnf = BUTTON_CONFIG)

label_hamburger =  Label(window2, text=0, font=("Lora Italic",18) , cnf = BUTTON_CONFIG)

label_frenchfries =  Label(window2, text=0, font=("Lora Italic",18) , cnf = BUTTON_CONFIG)




label_pasta.place(x=280,y=18+SIZE*0)
label_stramboli.place(x=280,y=180+SIZE*0)
label_hamburger.place(x=280,y=340+SIZE*0)
label_frenchfries.place(x=280,y=500+SIZE*0)




label1 = Label(window2 , text= "پاستا آلفردو",        font=("Lalezar",20) ,          cnf = BUTTON_CONFIG)

label2 = Label(window2 , text="800,000",        font=("Lalezar",16) ,          cnf = BUTTON_CONFIG)

label3 = Label(window2 , text= "استرامبولی"  ,        font=("Lalezar",20) ,          cnf = BUTTON_CONFIG)
label4 = Label(window2 , text="750,000"  ,        font=("Lalezar",16) ,          cnf = BUTTON_CONFIG)
label5 = Label(window2 , text="همبرگر "         ,      font=("Lalezar",20),          cnf = BUTTON_CONFIG)
label6 = Label(window2 , text="900,000 "         ,      font=("Lalezar",16),          cnf = BUTTON_CONFIG)
label7= Label(window2 , text="سیب زمینی سرخ شده",      font=("Lalezar",20) ,        cnf = BUTTON_CONFIG)
label8= Label(window2 , text="300,000",      font=("Lalezar",16) ,        cnf = BUTTON_CONFIG)

label1.place(x=800,y=60+SIZE*0 )
label2.place(x=580,y=60+SIZE*0 )
label3.place(x=800,y=220+SIZE*0)
label4.place(x=580,y=220+SIZE*0)
label5.place(x=800,y=380+SIZE*0)
label6.place(x=580,y=380+SIZE*0)
label7.place(x=730,y=540+SIZE*0)
label8.place(x=580,y=540+SIZE*0)


button_pasta_minus = Button(window2, text='-', font=('',18),command=lambda : add(label_pasta, -1), cnf = BUTTON_CONFIG)

button_pasta_plus = Button(window2, text='+', font=('',18), command=lambda : add(label_pasta, 1), cnf = BUTTON_CONFIG)

button_stramboli_minus = Button(window2, text='-', font=('',18),command=lambda : add(label_stramboli, -1), cnf = BUTTON_CONFIG)

button_stramboli_plus = Button(window2, text='+', font=('',18), command=lambda : add(label_stramboli, 1), cnf = BUTTON_CONFIG)

button_hamburger_minus = Button(window2, text='-', font=('',18),command=lambda : add(label_hamburger, -1), cnf = BUTTON_CONFIG)

button_hamburger_plus = Button(window2, text='+', font=('',18), command=lambda : add(label_hamburger, 1), cnf = BUTTON_CONFIG)

button_frenchfries_minus = Button(window2, text='-', font=('',18),command=lambda : add(label_frenchfries, -1), cnf = BUTTON_CONFIG)

button_frenchfries_plus = Button(window2, text='+', font=('',18), command=lambda : add(label_frenchfries, 1), cnf = BUTTON_CONFIG)

button_pasta_minus.place(x=220,y=60)

button_pasta_plus.place(x=330,y=60)

button_stramboli_minus.place(x=220,y=220)

button_stramboli_plus.place(x=330,y=220)

button_hamburger_minus.place(x=220,y=380)

button_hamburger_plus.place(x=330,y=380)

button_frenchfries_minus.place(x=220,y=540)

button_frenchfries_plus.place(x=330,y=540)


button_change_to_3 = Button(window2, text="صفحه بعد", font=("", 18), command=change_window_to_3, cnf=BUTTON_CONFIG)
button_change_to_3.place(x=450, y=700)







window3 = Toplevel(root)
window3.protocol("WM_DELETE_WINDOW", root.destroy)
window3.withdraw()
window3.geometry('1000x1500')
window3.config(bg="#333333")




total_label3 = Label(window3, text="جمع کل: 0", font=("Lalezar",22), cnf=BUTTON_CONFIG)
total_label3.place(x=400,y=900)

img_soup = Image.open(r'C:/Users/KMCC/Desktop/foods/images11.jpg')   
img_Coka = Image.open(r'C:/Users/KMCC/Desktop/foods/images13.jpg')
img_doogh = Image.open(r'C:/Users/KMCC/Desktop/foods/images9.jpg')
img_delester = Image.open(r'C:/Users/KMCC/Desktop/foods/images10.jpg')





img_soup=img_soup.resize((SIZE,SIZE))
img_Coka =img_Coka.resize((SIZE,SIZE))
img_doogh=img_doogh.resize((SIZE,SIZE))
img_delester=img_delester.resize((SIZE,SIZE))




img_soup = ImageTk.PhotoImage(img_soup)
img_Coka = ImageTk.PhotoImage(img_Coka)
img_doogh = ImageTk.PhotoImage(img_doogh)
img_delester = ImageTk.PhotoImage(img_delester)






button_soup = Button(window3 , image=img_soup, cnf = BUTTON_CONFIG)
button_Coka = Button(window3 , image=img_Coka, cnf = BUTTON_CONFIG)
button_doogh = Button(window3 , image=img_doogh, cnf = BUTTON_CONFIG)
button_delester = Button(window3 , image=img_delester, cnf = BUTTON_CONFIG)





button_soup.place(x=50,y=10+SIZE*0,width=SIZE,height=SIZE )
button_Coka.place(x=50,y=10*2+SIZE*1,width=SIZE,height=SIZE )
button_doogh.place(x=50,y=10*3+SIZE*2,width=SIZE,height=SIZE )
button_delester.place(x=50,y=10*4+SIZE*3,width=SIZE,height=SIZE )





label_soup =  Label(window3, text=0, font=("Lora Italic",18) , cnf = BUTTON_CONFIG)

label_Coka =  Label(window3, text=0, font=("Lora Italic",18) , cnf = BUTTON_CONFIG)

label_doogh =  Label(window3, text=0, font=("Lora Italic",18) , cnf = BUTTON_CONFIG)

label_delester =  Label(window3, text=0, font=("Lora Italic",18) , cnf = BUTTON_CONFIG)




label_soup.place(x=280,y=18+SIZE*0)
label_Coka.place(x=280,y=180+SIZE*0)
label_doogh.place(x=280,y=340+SIZE*0)
label_delester.place(x=280,y=500+SIZE*0)




label1 = Label(window3 , text="سوپ",        font=("Lalezar",20) ,          cnf = BUTTON_CONFIG)

label2 = Label(window3 , text="110,000",        font=("Lalezar",16) ,          cnf = BUTTON_CONFIG)

label3 = Label(window3 , text="نوشابه"  ,        font=("Lalezar",20) ,          cnf = BUTTON_CONFIG)
label4 = Label(window3 , text="120,000"  ,        font=("Lalezar",16) ,          cnf = BUTTON_CONFIG)
label5 = Label(window3 , text="دوغ"         ,      font=("Lalezar",20),          cnf = BUTTON_CONFIG)
label6 = Label(window3 , text="100,000 "         ,      font=("Lalezar",16),          cnf = BUTTON_CONFIG)
label7= Label(window3 , text="دلستر",      font=("Lalezar",20) ,        cnf = BUTTON_CONFIG)
label8= Label(window3 , text="120,000",      font=("Lalezar",16) ,        cnf = BUTTON_CONFIG)

label1.place(x=800,y=60+SIZE*0 )
label2.place(x=580,y=60+SIZE*0 )
label3.place(x=800,y=220+SIZE*0)
label4.place(x=580,y=220+SIZE*0)
label5.place(x=800,y=380+SIZE*0)
label6.place(x=580,y=380+SIZE*0)
label7.place(x=730,y=540+SIZE*0)
label8.place(x=580,y=540+SIZE*0)


button_pasta_minus = Button(window3, text='-', font=('',18),command=lambda : add(label_soup, -1), cnf = BUTTON_CONFIG)

button_pasta_plus = Button(window3, text='+', font=('',18), command=lambda : add(label_soup, 1), cnf = BUTTON_CONFIG)

button_stramboli_minus = Button(window3, text='-', font=('',18),command=lambda : add(label_Coka, -1), cnf = BUTTON_CONFIG)

button_stramboli_plus = Button(window3, text='+', font=('',18), command=lambda : add(label_Coka, 1), cnf = BUTTON_CONFIG)

button_hamburger_minus = Button(window3, text='-', font=('',18),command=lambda : add(label_doogh, -1), cnf = BUTTON_CONFIG)

button_hamburger_plus = Button(window3, text='+', font=('',18), command=lambda : add(label_doogh, 1), cnf = BUTTON_CONFIG)

button_frenchfries_minus = Button(window3, text='-', font=('',18),command=lambda : add(label_delester, -1), cnf = BUTTON_CONFIG)

button_frenchfries_plus = Button(window3, text='+', font=('',18), command=lambda : add(label_delester, 1), cnf = BUTTON_CONFIG)

button_pasta_minus.place(x=220,y=60)

button_pasta_plus.place(x=330,y=60)

button_stramboli_minus.place(x=220,y=220)

button_stramboli_plus.place(x=330,y=220)

button_hamburger_minus.place(x=220,y=380)

button_hamburger_plus.place(x=330,y=380)

button_frenchfries_minus.place(x=220,y=540)

button_frenchfries_plus.place(x=330,y=540)



total_label = Label(root, text="جمع کل: 0", font=("Lalezar",22), cnf=BUTTON_CONFIG)
total_label.place(x=400,y=900)
mainloop()






















# from tkinter import *
# from PIL import Image, ImageTk

# SIZE = 120

# root = Tk()
# root.geometry("600x600")
# root.title("منوی پیتزا")

# # اطلاعات پیتزاها
# pizzas = [
#     {"name": "پیتزا پپرونی", "price": 658000, "img": "C:/Users/KMCC/Desktop/foods/images.jpg"},
#     {"name": "پیتزا مرغ", "price": 550000, "img": "C:/Users/KMCC/Desktop/foods/images2.jpg"},
#     {"name": "پیتزا گوشت و قارچ", "price": 990000, "img": "C:/Users/KMCC/Desktop/foods/images3.jpg"},
#     {"name": "پیتزا مخصوص", "price": 730000, "img": "C:/Users/KMCC/Desktop/foods/uHhk8Ti_zWZightn.jpg"}
# ]

# counts = []
# images = []

# def update_total():
#     total = 0
#     for i in range(len(pizzas)):
#         total += int(counts[i]['text']) * pizzas[i]["price"]
#     total_label['text'] = f"جمع کل: {total}"

# def change_count(label, amount):
#     value = int(label['text']) + amount
#     if value < 0:
#         value = 0
#     label['text'] = value
#     update_total()

# for i, pizza in enumerate(pizzas):

#     y = 20 + i * 130

#     img = Image.open(pizza["img"])
#     img = img.resize((SIZE, SIZE))
#     img = ImageTk.PhotoImage(img)
#     images.append(img)

#     img_label = Label(root, image=img)
#     img_label.place(x=20, y=y)

#     name_label = Label(root, text=pizza["name"], font=("Arial",16))
#     name_label.place(x=160, y=y+20)

#     price_label = Label(root, text=f"قیمت: {pizza['price']}", font=("Arial",12))
#     price_label.place(x=160, y=y+50)

#     count_label = Label(root, text="0", font=("Arial",16))
#     count_label.place(x=350, y=y+40)
#     counts.append(count_label)

#     minus_btn = Button(root, text="-", font=("Arial",14),
#                        command=lambda l=count_label: change_count(l,-1))
#     minus_btn.place(x=320, y=y+40)

#     plus_btn = Button(root, text="+", font=("Arial",14),
#                       command=lambda l=count_label: change_count(l,1))
#     plus_btn.place(x=390, y=y+40)

# total_label = Label(root, text="جمع کل: 0", font=("Arial",18))
# total_label.place(x=200, y=550)

# root.mainloop()



# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QPixmap, QFont, QIcon
# from PyQt5.QtCore import Qt, QSize

# # --- تنظیمات استایل کلی برنامه ---
# STYLE_SHEET = """
#     QMainWindow { background-color: #f8f9fa; }
    
#     QScrollArea { border: none; background-color: transparent; }
    
#     #Card {
#         background-color: white;
#         border-radius: 20px;
#         border: 1px solid #e0e0e0;
#     }
    
#     #FoodTitle { font-size: 18px; font-weight: bold; color: #333; border: none; }
#     #FoodPrice { font-size: 15px; color: #666; border: none; }
#     #CounterLabel { font-size: 18px; font-weight: bold; border: none; }
    
#     #AddBtn, #MinusBtn {
#         background-color: #ff4757;
#         color: white;
#         border-radius: 10px;
#         font-size: 20px;
#         font-weight: bold;
#         min-width: 40px;
#         min-height: 40px;
#     }
#     #AddBtn:hover { background-color: #ff6b81; }
    
#     #OrderBtn {
#         background-color: #2ed573;
#         color: white;
#         font-size: 20px;
#         font-weight: bold;
#         border-radius: 15px;
#         padding: 15px;
#     }
#     #OrderBtn:hover { background-color: #7bed9f; }
    
#     #TotalLabel { font-size: 22px; font-weight: bold; color: #2f3542; margin: 10px; }
# """

# class PizzaCard(QFrame):
#     def __init__(self, name, price, img_path, main_app):
#         super().__init__()
#         self.setObjectName("Card")
#         self.main_app = main_app
#         self.name = name
#         self.price = price
#         self.count = 0

#         layout = QVBoxLayout(self)

#         # تصویر محصول
#         self.img_label = QLabel()
#         pix = QPixmap(img_path).scaled(180, 180, Qt.KeepAspectRatio, Qt.SmoothTransformation)
#         self.img_label.setPixmap(pix)
#         self.img_label.setAlignment(Qt.AlignCenter)
#         self.img_label.setStyleSheet("border: none;")

#         # اطلاعات محصول
#         self.title = QLabel(name)
#         self.title.setObjectName("FoodTitle")
#         self.title.setAlignment(Qt.AlignCenter)

#         self.price_lbl = QLabel(f"{price:,} تومان")
#         self.price_lbl.setObjectName("FoodPrice")
#         self.price_lbl.setAlignment(Qt.AlignCenter)

#         # کنترلرها
#         controls = QHBoxLayout()
#         self.btn_minus = QPushButton("-")
#         self.btn_minus.setObjectName("MinusBtn")
#         self.btn_plus = QPushButton("+")
#         self.btn_plus.setObjectName("AddBtn")
#         self.lbl_count = QLabel("0")
#         self.lbl_count.setObjectName("CounterLabel")
        
#         self.btn_plus.clicked.connect(self.add)
#         self.btn_minus.clicked.connect(self.remove)

#         controls.addStretch()
#         controls.addWidget(self.btn_minus)
#         controls.addWidget(self.lbl_count)
#         controls.addWidget(self.btn_plus)
#         controls.addStretch()

#         layout.addWidget(self.img_label)
#         layout.addWidget(self.title)
#         layout.addWidget(self.price_lbl)
#         layout.addLayout(controls)

#     def add(self):
#         self.count += 1
#         self.lbl_count.setText(str(self.count))
#         self.main_app.update_total()

#     def remove(self):
#         if self.count > 0:
#             self.count -= 1
#             self.lbl_count.setText(str(self.count))
#             self.main_app.update_total()

# class RestaurantApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("سیستم هوشمند سفارش پیتزا")
#         self.resize(900, 750)
#         self.setStyleSheet(STYLE_SHEET)

#         self.pizzas = [
#             ("پیتزا پپرونی", 120000, "C:/Users/KMCC/Desktop/foods/images.jpg"),
#             ("پیتزا مرغ و زیتون", 110000, "C:/Users/KMCC/Desktop/foods/images2.jpg"),
#             ("پیتزا رست‌بیف", 145000, "C:/Users/KMCC/Desktop/foods/images3.jpg"),
#             ("پیتزا مخصوص", 130000, "C:/Users/KMCC/Desktop/foods/uHhk8Ti_zWZightn.jpg"),
#             ("پیتزا یونانی", 115000, "C:/Users/KMCC/Desktop/foods/images.jpg"), # تکرار برای تست اسکرول
#             ("پیتزا چهار فصل", 160000, "C:/Users/KMCC/Desktop/foods/images2.jpg")
#         ]

#         # چیدمان اصلی
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#         main_layout = QHBoxLayout(central_widget)

#         # --- سمت چپ: منو (Scrollable) ---
#         scroll = QScrollArea()
#         scroll.setWidgetResizable(True)
#         menu_content = QWidget()
#         self.grid = QGridLayout(menu_content)
        
#         self.cards = []
#         for i, (name, price, img) in enumerate(self.pizzas):
#             card = PizzaCard(name, price, img, self)
#             self.cards.append(card)
#             self.grid.addWidget(card, i // 2, i % 2) # چیدمان دو ستونه

#         scroll.setWidget(menu_content)
#         main_layout.addWidget(scroll, 2) # وزن بیشتر به منو

#         # --- سمت راست: سبد خرید و جمع کل ---
#         right_panel = QVBoxLayout()
        
#         cart_title = QLabel("🛒 سبد خرید شما")
#         cart_title.setStyleSheet("font-size: 22px; font-weight: bold; color: #ff4757;")
        
#         self.total_lbl = QLabel("جمع کل: 0 تومان")
#         self.total_lbl.setObjectName("TotalLabel")

#         self.btn_order = QPushButton("ثبت و پرداخت نهایی")
#         self.btn_order.setObjectName("OrderBtn")
#         self.btn_order.clicked.connect(self.checkout)

#         right_panel.addWidget(cart_title)
#         right_panel.addStretch()
#         right_panel.addWidget(self.total_lbl)
#         right_panel.addWidget(self.btn_order)

#         main_layout.addLayout(right_panel, 1)

#     def update_total(self):
#         total = sum(card.count * card.price for card in self.cards)
#         self.total_lbl.setText(f"جمع کل: {total:,} تومان")

#     def checkout(self):
#         receipt = "--- فاکتور نهایی رستوران ---\n\n"
#         total = 0
#         has_items = False
        
#         for card in self.cards:
#             if card.count > 0:
#                 cost = card.count * card.price
#                 receipt += f"🔹 {card.name}: {card.count} عدد -> {cost:,} تومان\n"
#                 total += cost
#                 has_items = True
        
#         if not has_items:
#             QMessageBox.warning(self, "خطا", "سبد خرید شما خالی است!")
#             return

#         receipt += f"\n---------------------------\n💰 مبلغ قابل پرداخت: {total:,} تومان"
        
#         msg = QMessageBox()
#         msg.setWindowTitle("تایید سفارش")
#         msg.setText(receipt)
#         msg.setIcon(QMessageBox.Information)
#         msg.setStandardButtons(QMessageBox.Ok)
#         msg.exec_()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     # تنظیم فونت فارسی اگر روی سیستم داری (مثل Tahoma یا Samim)
#     app.setFont(QFont("Tahoma", 10))
#     window = RestaurantApp()
#     window.show()
#     sys.exit(app.exec_())
