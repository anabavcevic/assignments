print( 35 * '#')
print("WELCOME TO DBS")
print( 35 * '#')
      
number1 = input("Enter number1: ")
number2 = input("Enter number2: ")
sum = parse(number1)+parse(number2)
print("Total is:",sum)

def parse(number):
  if (not number.isdigit()):
    return -1
  return int(number)

