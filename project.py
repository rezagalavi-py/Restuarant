
# from random import choice
# choices= ['sang','kaghaz','gheichi']
# computer_choice = choice(choices)
# message = f"choose from {choices} :"
# user_choice = input(message)
# if computer_choice==user_choice:
#     print("It's tie!")
# elif (computer_choice , user_choice) in [('kaghaz','sang'),('gheichi','kaghaz'),('sang','gheichi')]:
#     print(" You lose")
# else:
#     print("You win")

# print(f"{computer_choice=},{user_choice=}")






# پروژه صندوقدار فروشگاه

# cart =[]
# items = {
#     'chips': 180000,
#     'pofak': 150000,
#     'roghan': 220000,
#     'macaroni': 230000,
#     'morgh': 1230000,
#     'berenj': 5000000,
#     'saboon': 90000,
#     'nooshabe': 150000,
#     'doogh': 120000,
# }
# i=1
# factor={}

# answer = input(f"Enter item {i}:").strip()
# while answer!="":
#     if answer in items:
#         factor.setdefault(answer,0)
#         factor[answer]+=1
#         i+=1
#     answer = input(f"Enter item {i}:").strip()
# total = 0
# for name, amount in factor.items():
#     p = items.get(name)
#     cart.append(f"Item:{name:<20}, price:{p:<8}, Amount:{amount:<1}, total:{p*amount:<10}")
#     total+=p*amount
# for row in cart:
#     print(row)

# print(total)









# cart = []
# items ={
#     'doogh': 200000,
#     'chips': 175000,
#     'soosis': 250000,
#     'pofak': 180000,
#     'mast': 290000,
#     'berenj': 5000000,
#     'morgh': 1300000,
#     'saboon': 160000,
# }
# i=1
# factor ={}
# answer = input(f"Enter item {i} :")

# while answer!="":
#     if answer in items:
#         factor.setdefault(answer,0)
#         factor[answer]+=1
#     i+=1
#     answer = input(f"Enter item {i} :")
# print(factor)    

# for name, amount in factor.items():
#     cart.append(f" Items:{name:}")




# def alaki(n):
#     print(1)
#     print(2)
#     print(3)
#     print(4)
#     print(n)
#     print('end')

# for i in range(3):
#     name = input("Enter your name :")
#     alaki(name)


# from os import system 
# system('os')

# def add_sum_number(a,b,c=0):
#     return a+b+c

# print(add_sum_number(7,8,10))
# print(add_sum_number(2,1))



# پروژه وارد کردن رمز
# from string import punctuation
# def is_secure(password:str):
#     if len(password)<8:
#         return False
#     if password.isupper():
#         return False
#     if password.islower():
#         return False
#     if password.isalpha():
#         return False
    
#     result = set(punctuation).intersection(set(password))
#     if result==0:
#         return False
#     return True

# for i in range(10):
#     p = input("Enter password: ")
#     if is_secure(p):
#         print(f"{p} is a secure paasword")
#     else:
#         print(f"{p} is not a secure paasword")


# def calculate_time(distance: float , velocity: float)-> float:
#     return round(distance/velocity, 2)

# print (calculate_time(1000,900))


#پیدا کردن رمز
# import os

# import string

# os.system('cls')

# real_password= "4l56"
# found=False
# letters = string.ascii_lowercase+string.digits
# for i in letters:
#     for j in letters:
#         for k in letters:
#             for z in letters:
#                 print(i+j+k+z)
#                 if i+j+k+z == real_password:
#                     print(f'password is {i+j+k+z}')
#                     found=True
#                     break
#             if found== True:
#              break      
#         if found== True:
#             break      
#     if found== True:
#             break      


# n = float(input("Enter number :"))
# try:
#     print(20/n)
# except:
#     print("I cant divid by 0")

# open('t.txt','w')
# open('project/t.txt','w')



# پروژه دفترجه تلفن
import json
import os
os.system('cls')


def save():
    f = open('contacts.json','w')
    json.dump(contacts,f,indent=4)
    f.close()
def load():
    try:
       f = open('contacts.json','r')
       contacts= json.load(f)
       return contacts
    except:
        return{}
contacts = {
    "Ali": '09151234569',
}

while True:
    name = input("Enter name :").capitalize()
    if name =="0":
        break
    if name in contacts:
       print(contacts.get(name))
    else:
        answer = input("This contact dosen't exist in contacts list.\nDo you want to add his/her?")
        while answer not in ["yes","y","no","n"]:
            answer = input("This contact dosen't exist in contacts list.\nDo you want to add his/her?") 
        if answer in["yes","y"]:
            number = input("Enter number :")
            contacts[name]=number

save()





















