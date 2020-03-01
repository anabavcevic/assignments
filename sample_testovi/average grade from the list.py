grade= [] # initialising list
num = float(input("enter the first grade: "))
grade.append(num)
num= float (input("Enter the second grade: "))
grade.append(num)
num= float(input("Enter the third grade: "))

average = sum(grade) / len(grade)
print("average grade is: ", average)