# for i in range(10):
#     print(i*2)

# for i in range(50):
#     print("Salam")

# for i in range(3):
#     print(f"{i+2}")


import os
os.system('cls')

# for i in range(10):
#     print(f" Enter number {i+1}:")

# for i in range(10,20, 2):
#     print(f" Enter number{i}")

# from time import sleep  
# for i in range(10,0,-1):
#     print(f"{i}")
#     sleep (0.25)

# for i in ['ali','reza','neda','sara']:
#     print(i)

# for i in "reza":
#     print(i)

# foods={
#     'pasta' : '500000',
#     'pizza' : '650000',
#     'humberger': '750000',
# }

# # for item in foods.items():
# #     print(item)

# for (name,price) in foods.items():
#     print(f"price of {name} is {price}")

# from random import randint
# import os
# os.system('cls')

# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))

# guess = randint(a,b) #99
# n = 0
# for i in range(100):
#     s = input(f"Is it {guess}? [>   <   =]")
#     n+=1
#     if s == "=":
#         print("WOW! I found answer!")
#         break
#     elif s == ">":
#         a = guess+1
#         guess= randint(a,b)
       

#     elif s== "<":
#         b = guess-1
#         guess= randint(a, b)
#     else:
#         print(" I can't understand...")

# print(f" I fount the answer in {n} times.")

# s = 0 
# number = input("Enter a number :")
# for digit in number:
#     s = s+int(digit)

# print(s)

# a = 0
# while True:
#      print('ok')
#      a+=1
#      if a==6:
#         break
    
# print('end')
        
# a=0
# while a!=5:
#     print('ok')
#     a+=1
# print('end')

 


# secret_password = "python" 
# user_input =""

# while user_input!= secret_password:
#     # user_input = input("please enter passcode:")
#     if user_input == secret_password:
#         break
# print("succesfully")
cart =[]
items = {
    'chips': 180000,
    'pofak': 150000,
    'roghan': 220000,
    'macaroni': 230000,
    'morgh': 1230000,
    'berenj': 5000000,
    'saboon': 90000,
    'nooshabe': 150000,
    'doogh': 120000,
}
i=1
factor={}

answer = input(f"Enter item {i}:").strip()
while answer!="":
    if answer in items:
        factor.setdefault(answer,0)
        factor[answer]+=1
        i+=1
    answer = input(f"Enter item {i}:").strip()
total = 0
for name, amount in factor.items():
    p = items.get(name)
    cart.append(f"Item:{name:<20}, price:{p:<8}, Amount:{amount:<1}, total:{p*amount:<10}")
    total+=p*amount
for row in cart:
    print(row)

print(total)