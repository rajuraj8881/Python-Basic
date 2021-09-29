# salary = 5300
# vacation_day = 35
# if salary > 5000 and vacation_day > 40:
#     print("I well take this job")
# else:
#     print("This job sucks! Give it to Jerry")

# age = 29
# huge_headphone = True
# if age > 30 and huge_headphone == True:
#     print("Must be Chuck Norris.")
# else:
#     print("SOC, son of Chuck Norris.")
# planetY = 40
# fireY = 30
# planetX = 50
# fireX = 40
# redius = 40
# if (planetY - fireY) < redius and (planetX - fireX) < redius:
#     print("distroy planet")

# money_text = input(500.5)
# money = float(money_text)
# print(money)

# x = 2
# y = 3
# z = (x + 2) * y
# print(y + z)

# name = input("Raju Mondal")
# print(name)

# age_text = input(10)
# age = int(age_text)
# print(age)

# a = 5
# b = 2
# x = a + b
# y = a % b
# z = a / b
# print(x, y, z)

# age = 20
# if age <= 5:
#     print("Watch tom and jerry")
# elif age <= 10:
#     print("Read comic books")
# elif age <= 18:
#     print("Watch family movie")
# else:
#     print("Do whatever you want")

# a = 5
# b = 7
# c = b = a
# print(b)

# count = '69'
# count = int(count)
# print(count)

# x = 5
# y = 7
# z = (x + y) * (x - y)
# Z = 21
# print(z)

# money = 25
# families = 7
# money_lift = money % families
# print(money_lift)

#list
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# # print(mylist[2:])
# if "cherry" in mylist:
#     print("Yes, 'apple' is in the fruits list")
# else:
#     print("Fruits not in the list")

#Change Item Value
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# mylist[2:1] = ["blackcurrant", "blackcurrant2"]
# print(mylist)

#Append Items
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# mylist.append("blackcurrant")
# print(mylist)

# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# mylist.insert(0, "blackcurrant")
# print(mylist)

# mylist = ["apple", "banana", "cherry"]
# mylist2 = ["orange", "kiwi", "melon", "mango"]
# mylist.extend(mylist2)
# print(mylist)

# mylist = ["apple", "banana", "cherry"]
# mylist2 = ("orange", "kiwi", "melon", "mango")
# mylist.extend(mylist2)
# print(mylist)

#Remove Specified Item
# mylist = ["apple", "banana", "cherry"]
# mylist.remove("banana")
# print(mylist)

# Remove Specified Index *****************************************
# mylist = ["apple", "banana", "cherry"]
# mylist.pop(0)
# print(mylist)

# Python - Loop Lists *****************************************
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# for x in mylist:
#     print(x)

#Loop Through the Index Numbers *****************************************
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# for x in range(len(mylist)):
#     print(mylist[x])

#Using a While Loop *****************************************
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# i = 0
# while i < len(mylist):
#     print(mylist[i])
#     i = i + 1

#Looping Using List Comprehension *****************************************
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# [print(x) for x in mylist]

#List Comprehension *****************************************
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# newlist = []
# for x in mylist:
#     if 'm' in x:
#         newlist.append(x)
# print(newlist)

# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# newlist = [x for x in mylist if 'a' in x]#newlist = [expression for item in iterable if condition == True]
# print(newlist)

#Sort List Alphanumerically *****************************************
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# mylist.sort()
# print(mylist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

#Sort Descending
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)

#Python - Copy Lists
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

#Join Two Lists
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# for x in list2:
#     list1.append(x)
#
# print(list1)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)

#Python Functions *****************************************
# def my_function(fname):
#     print("My name is " + fname)
# my_function("Raju Mondal")
# my_function("Readoy Baroy")

#Python Arrays *****************************************
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# x = mylist[2]
# print(x)

# x = len(mylist)
# print(x)

#Looping Array Elements
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# mylist.append("raju")
# mylist.pop(0)
# mylist.remove("banana")
# for x in mylist:
#     print(x)

#Python Classes and Objects *****************************************
# class MyClass:
#     x = 5
# test = MyClass()
# print(test.x)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age  = age
#
# man = Person("Readoy", 16)
# print(isinstance(man, Person))
# print(man.name, man.age)

# class Person:
#     def __init__(myself, name, age):
#         myself.name = name
#         myself.age  = age
#     def myfunction(abc):
#         print("My name is " + abc.name + " age " + str(int(abc.age)))
# name = Person("Readoy", 10)
# name.myfunction()

#Python Inheritance *****************************************
# class Person:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname  = lastname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
# class Student(Person):
#     pass
#
# user = Student("Readoy", "Barroy")
# user.printname()

# class Person:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#     def printname(self):
#         print(self.firstname, self.lastname)
# class Student(Person):
#     def __init__(self, firstname, lastname, year):
#         # Person.__init__(self, firstname, lastname)
#         # alternative on Person class
#         super().__init__(firstname, lastname)
#         self.year = year
#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, " to the class of", self.year)
# student = Student("Readoy", "Barroy", 2021)
# student.welcome()

#Python JSON

import json
# x = '{ "name":"John", "age":30, "city":"New York" }'
# # y = json.loads(x)
# y = json.dumps(x)
# print(y)

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# x = {
#     "name": "John",
#     "age": 30,
#     "married": True,
#     "divorced": False,
#     "children": ("Ann", "Billy"),
#     "pets": None,
#     "cars": [
#         {"model": "BMW 230", "mpg": 27.5},
#         {"model": "Ford Edge", "mpg": 24.1}
#       ]
# }
#
# y = json.dumps(x, indent=4, separators=(", ", " = "))
# print(y)

import camelcase
try:
    c = camelcase.CamelCase()

    txt = "hello world"

    print(c.hump(txt))
except:
    print("An exception occurred")