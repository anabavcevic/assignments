# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:09:00 2020

@author: Ana
"""

def format_something(num, format_string):
    print(">" + format_string.format(num) + "<")

format_something(124587.259, "${0:,.2f}")
format_something(124587.259, "${0:,.4f}")
format_something(124587.259, "${0:.2f}")
format_something(124587.259, "${0:,f}")
format_something(124587.259, "${0:0f}")
format_something(124587.259, "${0:.0f}")
format_something(124587.259, "${0:,.0f}")
format_something(-124587.259, "${0:,.2f}")

format_something('hello how are you?', "{:10}")
format_something('hello', "{:10}")
format_something('hello', "{:_<10}")
format_something('hello', "{:^10}")
format_something('hello how are you?', "{:.10}")
format_something('hello how are you?', "{:10.7}")
