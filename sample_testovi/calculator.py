# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 19:56:27 2020

@author: Ana
"""

import math

print('Available operators: +, -, *, /, root, exp, log, cos, sin, tan')

v_operator = input('put operator:')

def add():
    first_num = float(input('input first number:'))
    second_num = float(input('input second number:'))
    return first_num + second_num

def sub():
    first_num = float(input('input first number:'))
    second_num = float(input('input second number:'))
    return first_num - second_num

def multy():
    first_num = float(input('input first number:'))
    second_num = float(input('input second number:'))
    return first_num * second_num

def divide():
    first_num = float(input('input first number:'))
    second_num = float(input('input second number:'))
    return first_num / second_num

def exp():
    first_num = float(input('input first number:'))
    second_num =float(input('input an exponent: '))
    return first_num ** second_num

def n_root():
    first_num = float(input('input a number you want to calculate a root from:'))
    second_num = float(input('input a degree of root: '))
    return first_num ** (1 / second_num)

def logN():
    first_num = float(input('input a number: '))
    second_num = float(input('input a base: '))
    return math.log(first_num, second_num)

def sin():
    first_num = float(input('input number you want to calculate a sin of: '))
    return math.sin(first_num)

def cos():
    first_num = float(input('input number you want to calculate a cos of: '))
    return math.cos(first_num)

def tan():
    first_num = float(input('input number you want to calculate a tangens of: '))
    return math.tan(first_num)

    

if v_operator == '+':
    print("sum = {0:.3f}".format(add()))
if v_operator == '-':
    print(sub())
if v_operator == '*':
    print(multy())
if v_operator == '/':
    print(divide())
if v_operator == '**':
    print(exp())
if v_operator == 'root':
    print(n_root())
if v_operator == 'log':
    print(logN())
if v_operator == 'sin':
    print(sin())
if v_operator == 'cos':
    print(cos())
if v_operator == 'tan':
    print(tan())
    
    
import unittest
class ExamTest(unittest.TestCase):
    def test_claculate(self):
        self.assertEqual(21, calculate_digit_sum(678))
unittest.main()

    
    



