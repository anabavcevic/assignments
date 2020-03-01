# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 16:37:46 2020

@author: Ana
"""

class Book:
    def __init__(self,title, code):
        self.__title = title
        self.__code = code
    def getTitle(self):
        return self.__title
    def getCode(self):
        return self.__code


outfile = open("C:\\Users\\Ana\\Desktop\\prosli testovi\\book1_out.csv", 'a')

book_title= input("Enter the title of the book: ")
book_code= input("Enter the code of the book: ")

abook = Book(book_title, book_code)

with open("C:\\Users\\Ana\\Desktop\\prosli testovi\\book1_out.csv", 'a') as myfile:
    myfile.write(abook.getTitle() + "," + abook.getCode())


  
    
