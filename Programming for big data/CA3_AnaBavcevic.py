# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
# GITHUB repository: https://github.com/anabavcevic/assignments/blob/master/Programming%20for%20big%20data/CA3_AnaBavcevic.py


from functools import reduce
import math
import unittest


print('Available operators: +, -, *, /, root, exp, log, cos, sin, tan')

v_operator = input('put operator:')
first = float(input('input first number:'))
second = float(input('input second number:'))
a = [1,2,3,4,5,6]
b = [9,8,7,4,5,6]



if v_operator == '+':
    add()
if v_operator == '-':
    sub()
if v_operator == '*':
    multy()
if v_operator == '/':
    divide()
if v_operator == '**':
    exp()
if v_operator == 'root':
    n_root()
if v_operator == 'log':
    logN()
if v_operator == 'sin':
    sin()
if v_operator == 'cos':
    cos()
if v_operator == 'tan':
    tan()
    
    

class Calculator:
    
################################# MAP ###############################
    def add(first, second):
        return map(lambda x, y: x+y, first, second)

    def sub():
        return map(lambda x, y: x-y, a,b)

    def multy():
        return map(lambda x, y: x-y, first, second)

############################ LIST COMPREHENTION ###################################
        
    def logN():
        return [math.log(x, y) for x, y in ((first, second))]
    def divide():
        return [(x/y) for x,y in (( a,b))]

########################### GENERATE ##############################################

    def sin(v_operator):
        counter = 0
        while True:
            if(counter > v_operator):
                return ("Finished")
            yield (lambda x, y: math.sin(x), first)
            counter +=1

    def cos(v_operator):
        counter = 0
        while True:
            if(counter > v_operator):
                return ("Finished")
            yield (lambda x: math.cos(x), first)
            counter +=1
        
    def tan(v_operator):
        counter = 0
        while True:
            if(counter > v_operator):
                return ("Finished")
            yield (lambda x: math.tan(x), first)
            counter +=1       

########################### REDUCE ################################################

    def exp():
        answer = reduce(lambda x, y: x**y, [1,2,3,4,5,6])
        return answer

    def n_root():
        answer = reduce(lambda x, y: x**(1/y), [5,25,8,2,7,49])
        return answer
    
#####################################################################
        
 
    
#import unittest
#class ExamTest(unittest.TestCase):
#    def test_claculate(self):
#       self.assertEqual(21, calculate_digit_sum(678))
#unittest.main()

class Test_Calc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(15, add(5,10))
    def test_sub(self):
        self.assertEqual(10, sub(15,5))
    def test_multy(self):
        self.assertEqual(25, multy(5,5))
    def test_divide(self):
        self.assertEqual(2, divide(4,2))
    def test_logN(self):
        self.assertEqual(1, logN(10,10))
    def test_sin(self):
        self.assertEqual(0.17, sin(10))
    def test_cos(self):
        self.assertEqual(0.98, cos(10))
    def test_tan(self):
        self.assertEqual(0.17, tan(10))
    def test_exp(self):
        self.assertEqual(4, exp(2,2))
    def test_n_root(self):
        self.assertEqual(5, n_root(2,25))
        
        
if__name__=='__main__':
    unittest.main()
    


