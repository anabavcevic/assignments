#km to miles
print( 35 * '#')
print("WELCOME TO DBS")
print( 35 * '#')
      
print("Menu options")


print("1 - Convert Kilometers to Miles")
print("2 - Convert ~Miles to Kilometers")

izbor = input('Enter Menu choice: ')

if izbor == "1":
    udaljenost =  input('Enter the value in Kilometers: ')
    nova_udaljenost= float(udaljenost) * 0.62
    print(udaljenost , "Kilometers in Miles is: " , nova_udaljenost)

if izbor == "2":
    udaljenost =  input('Enter the value in Miles: ')
    nova_udaljenost= float(udaljenost) / 0.62
    print(udaljenost , "Kilometers in Miles is: " , nova_udaljenost)
    


