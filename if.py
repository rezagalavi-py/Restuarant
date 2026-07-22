# import os
# os.system('cls')
# a = input("Enter password 1:")
# b = input("Enter password 2 :")
# c = input("Enter password 3:")
# d = input("Enter password 4:")
# if a == "123":
      
#     if b=="456":
#         if c=="789":
#             if d =="0":
#                  print("Welcom...")
#             else:
#                  print("Wrong password 4")
#         else:
#               print("Wrong password 3")
#     else:
#          print("Wrong password 2")          
# else:
#     print("Wrong password 1")          
    
# print("END")





# import os
# os.system('cls')


# a= input("Enter password 1 :")
# b= input("Enter password 2 :")
# c= input("Enter password 3 :")
# d= input("Enter password 4 :")

# if a=="123":
#     if b=="456":
#         if c=="789":
#             if d =="0":
#                 print("WELCOM...")
#             else:
#                 print("Wrong password")    
#         else:
#              print("Wrong password") 
#     else:
#              print("Wrong password")         
# else:
#     print("Wrong password")         

# print("END")


import os
os.system('cls')


# a= input("Enter password 1 :")
# b= input("Enter password 2 :")
# c= input("Enter password 3 :")
# d= input("Enter password 4 :")

# if a=="123" and b=="456" and c=="789" and d=="0":
#     print("WELCOME...")
# else:
#     print("Wrong password")

# print("END")


# from random import randint, choice
# a= randint(1,2)
# if a== 1:
#     gol="left"
# else:
#     gol="right"

# user=input("Right or Left?").lower().strip()

# if user == gol:
#     print(f"{10*'-'} YOU win {10*'-'}")
# else:
#     print(f"{10*'-'} YOU lose {10*'-'}")


# a =input("Enter word:")
# b = list(a)
# b.reverse()
# if b==list(a):
#     print(f"{a} is pallindrom")
# else:
#     print(f"{a} is not pallindrom")

# from random import randint, choice

# a =int(input("Enter a number:"))
# b = int(input("Enter another number:"))
# if a>b:
#     a,b= b,a
# answer = randint(a,b)
# Guess =int(input(f"Guess number in range({a},{b})"))
# if Guess>answer:
#     print("your answer in bigger than{Guess}")
# elif Guess<answer:
#     print("your answer in smaller than{Guess}")
# elif Guess == answer:
#     print("You win")
# print(answer)

# username = input("Enter a username :")
# password = input("Enter a password :")
# password2 = input("Reapet a password :")
# if (password in username) or (username in password):
#     print("username and password can not in the same carector")


# grade= float(input("Enter a grade :"))

# if 17<=grade<20:
#     print("A")

# elif 14<=grade<17:
#     print("B")

# elif 12<=grade<14:
#     print("C")

# elif 10<=grade<12:
#     print("D")

# elif 5<=grade<10:
#     print("E")

# elif 0<=grade<5:
#     print("F")



# list1 =['Farvardin','Ordibehesht','Khordad','Tir','Mordad','Shahrivar']
# list2 =['Mehr','Aban','Azar','Dey','Bahman']
# list3=['Esfand']
# a = input("Enter month :").capitalize( )
# if a in list1:
#     print(f"{a} is 31 Days")
# elif a in list2:
#     print(f"{a} is 30 Days")
# else:
#     print(f"{a} is 29 Days")



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


my_list = ['ali', 'reza','sara','fatemeh','neda']

score = [15,17,20,12,10]

# for i in range(len(my_list)):
#     print(f"{my_list[i]}'s grade is{grades[i]}")


for name , grades in zip(my_list, score):
    print(f"{name}'s grade {grades}")

# for index, name in enumerate(my_list):
#     print(f"{name}'s grade is{score[index]}")