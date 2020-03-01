print( 35 * '#')
print("WELCOME TO DBS CONSOLE")
print( 35 * '#') 

    
lista = []
broj_elemenata = int(input("Enter the number of items to be stored in the list: "))

for i in range(broj_elemenata):
    num=input('Enter the value for item ' + str(i+1) + ': ')
    lista.append(num)

my_set = set(lista)

counter=0
for i in my_set:
    if lista.count(i)>1:
        counter +=1
print("The number of duplicate item found in the list is: ", counter)