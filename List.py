# mylist = ['pizza', 'pasta','pasta','humberger','fast food','butter']
# new_item = ['egg','pasta','rice','pizza','bannana']
# print(mylist)
# print(mylist[:5])
# print(mylist[:3])
# print(mylist[::-1]) # لیست تماما برعکس چاپ میکند
# mylist.append('soosis')
# print(mylist)
# a =input('Enter new Item : ')
# mylist.append(a)
# print(mylist)
# mylist.insert(2,a)
# print(mylist)
# mylist.remove('pasta')
# mylist.remove('pasta')
# mylist.remove('pasta')
# mylist.remove('pasta')
# mylist.remove('pasta')
# print(mylist)
# a= mylist.pop(3)
# print(mylist)
# print(a)
# mylist.extend(new_item)
# print(mylist)
# a= mylist.count('pasta')
# print(a)
# mylist=['3','2','6','98','524','88','5.4','9','10000']
# mylist.sort()
# print(mylist)
# mylist = ['pizza', 'pasta','pasta','humberger','fast food','butter']

# a = input('Enter new Item :')
# mylist.insert(2,a)
# print(mylist)

# a = mylist.pop(3)
# print(mylist)
# print(a)
# mylist.remove('pasta')
# mylist.remove('pasta')
# print(mylist)

# a = mylist.index('pasta')
# print(a)

# my_tuple= (1,2,3,4,5,6,7)
# print(type(my_tuple))
# a = my_tuple.index(5)
# print(a)
# a= my_tuple.count(4)
# print(a)


# foods = ['koofte','gheimeh','kabab','joojeh','ghormeh']
# price = [500000,300000,450000,400000,1000000]

# print(foods[3],price[3])
# print(foods[0], price[0])


# print(foods['gheimeh'])
# print('gheimeh', foods['gheimeh'])

# print(foods.items())
# print(foods.keys())
# print(foods.values())

# price = foods.pop('koofte')
# print(price)
# print(foods)


# foods ={
#     'koofte': 500000,
#     'gheimeh': 300000,
#     'kabab': 450000,
#     'joojeh': 400000,
#     'ghormeh': 1000000,
# }

# print(foods)
# print(foods['koofte'])

# print('ghormeh', foods['ghormeh'])

# contacts = {
#     'ali': '09301234657',
#     'reza':'09307789358',
#     'maman':'09151014721',
# }

# a = contacts
# contacts.clear()
# print(a)

# print(contacts.get('sara'))

# print(contacts.items())

# print(contacts.keys())
# print(contacts.values())

# number = contacts.pop('maman')
# print(number)
# print(contacts)

# item = contacts.popitem()
# print(item)

contacts = {
    'ali': '09301234657',
    'reza':'09307789358',
    'maman':'09151014721',
}


# contacts.update({'hasan':'091245698721'})
# print(contacts)

# contacts['hasan']= '09124568792'
# contacts['mostafa']= '091825492'
# contacts['ehsan']= '0912659821'
# contacts['elham']= '09102589647'
# print(contacts)
# contacts.setdefault('ehsan', '123')
# print(contacts)
# contacts.setdefault('maman','09151014721')
# print(contacts)

names = ['ali', 'reza', 'sara', 'neda', 'elham']
contacts = dict.fromkeys(names, 'Tehran')
print(contacts)