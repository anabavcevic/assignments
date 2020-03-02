# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:30:42 2020

@author: Ana
"""

from functions import calculate_digit_sum
from functions import cube


import unittest
class ExamTest(unittest.TestCase):
    def test_claculate(self):
        self.assertEqual(21, calculate_digit_sum(678))
    def test_cube(self):
        self.assertEqual(8, cube(2))
        
unittest.main()
