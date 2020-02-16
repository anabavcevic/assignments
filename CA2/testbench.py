# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:14:55 2020

@author: Ana
"""

text = 'one\ntwo\nthree\nfour\ntwo\nthree'
contains = 'h'

new_text= text.split('\n')



index = 0
letter= 0
while index < len(new_text):
    if contains in new_text[index]:
        letter=letter+1
    index = index +1
print(letter)
    
        