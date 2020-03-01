# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:27:27 2020

@author: Ana
"""

hello ="my value"

def myfunction():
    print(hello)

def myfunction2(hello):
    print(hello)

def myfunction3():
    hello = 'filippo'
    print(hello)
    
def myfunction4():
    print('Hello ' + hello)

def myfunction5():
    global hello
    hello = 'filippo'

def myfunction6():
    print('Hello again ' + hello)


print(hello)

myfunction()

myfunction2('world')

myfunction3()

myfunction4()

myfunction5()

myfunction6()
