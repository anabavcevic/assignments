print( 35 * '#')
print("WELCOME TO DBS CONSOLE")
print( 35 * '#')

def calcsuma(num):
    suma = 0
    i=0
    while i<len(num):
        suma=suma + int(num[i])
        i=i+1
    return suma


num = input('Enter a number: ')
    
print("The sum of the digits of number " , num , " is " , calcsuma(num))