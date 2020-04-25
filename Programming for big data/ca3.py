# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:56:48 2020

@author: anabavcevic
"""
from functools import reduce

def add(first, second):
    return first + second

print(add(3,5))

add = lambda x, y : x+y

print(add(1,1))

square  = lambda x : x*x

print(square(2))

result = list(map(square, [1,2,3,4,5,6,7,8,9,10]))

print(result)
print(list(map(lambda x : x*x*x, [1,2,3,4,5,6,7,8,9,10])))

def fahrenheit(t):
    return((float(9)/5)*t+32)

def celsius(t):
    return(float(5)/9*(t-32))
temp = (36.5, 37, 37.5, 39)

F = list(map(fahrenheit, temp))
print(F)

C = list(map(celsius, F))
print(C)
print (list(map(lambda x: round (x, 2), C)))

a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
map(lambda x, y : x+y, a, b)
map(lambda x, y, z: x+y+z, a, b, c)
map(lambda x, y, z : x+y-z, a, b, c)

######################## FILTER ############################
fib = [0,1,1,2,3,5,8,13,34,55]

#return odd numbers
result = filter (lambda x : x%2, fib)
print(list(result))

#return even numbers
fib = [0,1,1,2,3,5,8,13,34,55]
result = filter (lambda x : x%2==0, fib)
print(list(result))


################ REDUCE #######################
#reduce is for list is being reduced to a single value - it returns one answer, not a list:
# it takes 2 rguments
# it will get a single result
#solution using reduce for sum 
answer = reduce(lambda x, y: x+y, [47,11,42,13])
print(answer)

#solution using produce for max
f = lambda a,b: a if(a>b) else b
reduce(f, [47,11,52,13])


#solution using produce for min
f = lambda a,b: a if(a<b) else b
reduce(f, [47,11,52,13])


###################################### LIST COMPREHENSION #########################
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [((float(9)/5*x+32) for x in Celsius)]
Fahrenheit
#Pitagora u comprehencion list s filterom:
[(x, y, z) for x in range(1,30) for y in range(x, 30) for z in range (y, 30) if x**2 + y**2 == z**2]

def pythagorean_triplet(max_value):
    values = []
    for x in range (1,max_value):
        for y in range(x, max_value):
            for z in range(y, max_value):
                if x**2 + y**2 == z**2:
                    values.append((x, y, z))
    return values

#big O notation for pythagorean_triplet
    
#O(n^3) 
#n is 30
pythagorean_triplet(30)

#cartouisan product

colours = ['red','green', 'yellow', 'blue']
things = ['house', 'car', 'tree']
coloured_things = [(x, y) for x in colours for y in things ]
print(coloured_things)


######################### GENERATOR #############################
 
def city_generator():
    yield("London")
    yield("Hamburg")
    yield("Konstanz")
    yield("Amsterdam")
    yield("Berlin")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")
    
    
city = city_generator()

print(next(city))
    

#### GENERATOR T CREATE FIBONACHI ##################

def fibonacci(n):
    #### gernerating fibonaci###
    a, b, counter = 0,1,0,
    while True:
        if(counter > n):
            return
        yield a
        a, b = b, a+b
        counter +=1
        
f = fibonacci(5)
for x in f:
    print(x, " ", end="" )
print()

f = fibonacci(15)

print(next(f))


######################## list comprehensions with yield #########################

def gen_pythagorean_triplets(max_value):
   
    for x in range (1,max_value):
        for y in range(x, max_value):
            for z in range(y, max_value):
                if x**2 + y**2 == z**2:
                    yield((x, y, z))


triplets = gen_pythagorean_triplets(10)
print(next(triplets))

triplets = gen_pythagorean_triplets(100)
for triplet in triplets:
    print(list(triplet))

#list comprehension with filter:
n = 30
n = 1000   
((x, y, z) for x in range(1,n) for y in range(x, n) for z in range (y, n) if x**2 + y**2 == z**2)

#genertator comprehension by using ()

triplet_comp = ()
((x, y, z) for x in range(1,n) for y in range(x, n) for z in range (y, n) if x**2 + y**2 == z**2)
for triplet in triplet_comp:
    print(triplet)
    

