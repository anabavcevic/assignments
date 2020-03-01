# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:39:47 2020

@author: Ana
"""

__firstname = ""
__lastname = ""

list = [
    { "gender": "M", "firstname": "Filippo", "lastname": "Possenti"},
    { "gender": "F", "firstname": "Ana", "lastname": "Bavcevic"}
]


def print_person_fullname():
    print(__firstname + " " + __lastname)

for p in list:
    __firstname = p["firstname"]
    __lastname = p["lastname"]
    print_person_fullname()



def print_fullname(p):
    if(p["gender"] == "M"):
        print("Mr " + p["firstname"] + " " + p["lastname"])
    else:
        print("Ms " + p["firstname"] + " " + p["lastname"])

for p in list:
    print_fullname(p)


class Person:
    def __init__(self, gender, firstname, lastname):
        self.__gender = gender
        self.__firstname = firstname
        self.__lastname = lastname
    def setFirstname(self, value):
        self.__firstname = value
    def setLastname(self, value):
        self.__lastname = value
    def setGender(self, value):
        self.__gender = value
    def getFirstname(self):
        return self.__firstname
    def printme(self):
        if(self.__gender == "M"):
            print("Mr " + self.__firstname + " " + self.__lastname)
        else:
            print("Ms " + self.__firstname + " " + self.__lastname)



list2 = [
    Person('M', "Filippo", "Possenti"),
    Person('F', "Ana", "Bavcevic")
]

for p in list2:
    p.printme()


