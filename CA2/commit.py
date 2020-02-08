# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 19:31:50 2020

@author: 99993
"""

class Commit:
    
    def __init__(self, details, comment=''):
        self.__id = details[0]
        self.__author = details[1]
        self.__date_time = details[2]
        self.__date = details[2].split(' ')[0]
        self.__time = details[2].split(' ')[1]
        self.__comment_lines = details[3]
        self.__comment = comment
        
    def __str__(self):
        return '"{0}","{1}","{2}","{3}","{4}","{5}"\n'.format(
            self.__id, self.__author,
            self.__date, self.__time,
            self.__comment_lines, self.__comment)
