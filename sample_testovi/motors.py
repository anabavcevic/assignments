# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:36:40 2020

@author: Ana
"""
import operator

file_name = 'C:/Users/Ana/Desktop/python/Motors.csv'

def get_data(file_name):
    data_file = open(file_name)
    data = data_file.readlines()
    data_file.close()
    return data


def calculate_average_wheel_base(data):
    cars = data[1:]
    num_cars = len(cars)
    total_wheel_base = 0
    #[1:] toforget the header - going form index 1 to the end, excluding 0
    #calculate average wheelbase
    for row in data[1:]:
        #strip for get rid of line endings
        #split string by ',' seperator into list
        #proccess index 3, i.e column D
        total_wheel_base += float(row.strip().split(',')[3])
        
    average_wheel_base = total_wheel_base / num_cars
    print('Average Wheel Base: {0}'.format(average_wheel_base))

def count_cars_per_manufacturer(data):
    cars_per_manufacturer = {} # instanciante a dictionary object
    for row in data[1:]:
        #get column B the masnufacturer and each time I see the mantacturer add one to the list
        manufacturer = row.strip().split(',')[1]
        if manufacturer in cars_per_manufacturer:
            cars_per_manufacturer[manufacturer] += 1
        else:
            cars_per_manufacturer[manufacturer] = 1
           
    for make in cars_per_manufacturer:
        print('{0} : {1}'.format(make, cars_per_manufacturer[make]))  
    return cars_per_manufacturer    

def get_max_selling_car(cars_per_manufacturer):  
    sorted_d = sorted(cars_per_manufacturer.items(),
        key = operator.itemgetter(1), reverse = True )
    print('dictionary in ascending order: ' , sorted_d)
    print(sorted_d[-1])


def get_car_details(data):
    matrix=[]
    data[0] = data[0].strip() + 'rltwb, hppam'
    
    for row in data[1]:
        row_data = row.strip().split(',')
        matrix.append(str(float(row_data[4])/ float(row_data[3])))
        matrix.append(str(float(row_data[7])/ float(row_data[8])))
    for row in matrix:
        print(row)
    return [data[0], matrix]

def save_car_details(car_details):
    save_file = open('C:/Users/Ana/Desktop/python/Motors.csv', 'w')
    save_file.write(car_details[0] + '\n')
      for row in car_details[1]:
        #converts to ',' separated string
        save_file.write(','.join(row) = '\n')
    
file_name = 'C:/Users/Ana/Desktop/python/Motors.csv'
data = get_data(file_name)
calculate_average_wheel_base(data)
cars_by_make = count_cars_per_manufacturer(data)
get_max_selling_car(cars_by_make)
car_details =  get_car_details(data)
save_car_details(car_details)
#exame- read the file, anc calculate the data- get sdata, pass the data, loop through it, and calculate something

#all the cars that are toyota- loop through the file and find manufacture and count them 

