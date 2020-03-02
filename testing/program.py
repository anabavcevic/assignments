# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:30:42 2020

@author: Ana
"""

from functions import calculate_digit_sum

def main():
    print(calculate_digit_sum(678))
    
    #print(calculate_digit_sum(11))
    
    print('#' * 20)
    print('Welcome to DBS console')
    print('#' * 20)
          
    value = input('Enter a number?')
    answer = calculate_digit_sum(value)
    print('The sum of the digits is: ?', answer)
main()
