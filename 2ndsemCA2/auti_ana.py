# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 11:51:53 2020

@author: Ana
"""
import csv
class CarStock(object):
    def __init__(self):
        self.__type = ''
        self.__totalcars = 0
        self.__rentedcars = 0
    
    def process_line(self, line):
        # split line and put the three values in three different variables of this class' instance
        columns = line.split(',')
        self.__type = columns[0]
        self.__totalcars = int(columns[1])
        self.__rentedcars= int(columns[2])
           
    def getType(self):
        return self.__type
  
    def getTotalCars(self):
        return self.__totalcars
    
    def getRentedCars(self):
        return self.__rentedcars
    
    def setRentedCars(self, value):
        self.__rentedcars = value
    
    def convert_objects_into_strings(self):
        return self.__type + ',' + str(self.__totalcars) + ',' + str(self.__rentedcars)



    
def convert_line(line):
    result = CarStock()
    result.process_line(line)
    return result

    
#read a file
def read_cars():
    changes_file = open('C:/Users/Ana/Documents/GitHub/assignments/2ndSem_CA2/cars.csv', 'r')
    lines = changes_file.readlines()
    changes_file.close()
    return lines


#write a file
def write_cars(lines):    
    csv_file = open('C:/Users/Ana/Documents/GitHub/assignments/2ndSem_CA2/cars2.csv', 'w')
    for line in lines:
        csv_file.write(line)
        csv_file.write('\n')
    
    csv_file.close()


def convert_cars(lines):
    results = []
    for line in lines:
        item = convert_line(line)
        results.append(item)
    return results

def convert_list_of_cars_into_list_of_strings(list_of_cars_stocks):
    result = []
    for item in list_of_cars_stocks:
        item = item.convert_objects_into_strings()
        result.append(item)
    return result




car_lines = read_cars()
stock_of_cars = convert_cars(car_lines)

reconverted = convert_list_of_cars_into_list_of_strings(stock_of_cars)

write_cars(reconverted)


#print(reconverted)


