# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:30:42 2020

@author: Ana
"""

class Functions:# for unit test to work I need to remove this class function and just leave a two functions
    def cube(self, number):
        cube_n= number**3
        return cube_n
    
    def calculate_digit_sum(self, value):
        total = 0
        for i in str(value): # this will automatically turne it to a string
            total = total + int(i)
        print(total)
        return total

