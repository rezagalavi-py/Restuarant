# class Person:
#     def __init__(self, name="Reza", surname="Mousavi", father_name="Mehdi", phone_number="09121326549"):
        
#         self.name= name
#         self.surname=surname
#         self.father_name=father_name
#         self.phone_number=phone_number


#     def __str__(self):
#         return f"Name :{self.name} {self.surname}\nfather name:{self.father_name}\nphone number:{self.phone_number}"
    
# p1=Person()
# p2=Person("Ali","galavi","Ahmad")
# p3=Person("Farshad","Eivary",phone_number="09121273898")
# print(p2)
# print(p1)
# print(p3)


# class Person:
#     def __init__(self, first_name,last_name,father_name):
#         self.first_name= first_name
#         self.last_name= last_name
#         self.father_name= father_name
       
 
#     def __str__(self):
#         return f"Hello, guys.\nI am {self.first_name} {self.last_name} and i am {self.weight}\nMy fateher name is {self.father_name}."

# class Student(Person):
#     def __init__(self, first_name, last_name, father_name, weight):
#         super().__init__(first_name, last_name, father_name)
#         self.weight= weight


# class Clerk(Person):
#     def __init__(self, first_name, last_name, father_name):
#         super().__init__(first_name, last_name, father_name)
  
#     def __str__(self):
#         return f"Hello, guys.\nI am {self.first_name} {self.last_name} \nMy fateher name is {self.father_name}."

# p1=Student("Ali","Mosavi","Mehdi","60")
# p2= Clerk("Reza","Maldar","Mani")

# print(p2)


# class Circle:
#     pi = 3.14
#     def __init__(self,r):
#         self.r = r
    
#     def get_area(self):
#         return 2*self.r*self.pi
    
# c1= Circle(50)
# s1=Circle(60)
# print(c1.get_area())
# print(s1.get_area())


# class Time():
#     def __init__(self, h=0 , m=0 , s=0):
#         self.h=h
#         self.m=m
#         self.s=s
#         if self.s>59:
#             self.m+=self.s//60
#             self.s%= 60
#         if self.m>59:
#             self.h+=self.m//60
#             self.m%= 60
#         if self.h >23:
#             self.h%=24

#     def __str__(self):
# #         return f"{self.h:02}:{self.m:02}:{self.s:02}"
# t= Time(28,20,350)

# print(t)


# def function():
#     global a
#     a=25
#     print(a)


# a = 20
# print(a)
# function()
# print(a)
# a = 30
# print(a)


# x=int(2.9)
# print(x)


list = [25,35,0,2,8,80,100,64,46]
list.sort()
print(list)