
print( 35 * '#')
print("WELCOME TO DBS")
print( 35 * '#')    
print("Accept a grade and display equivalent description: ")
print( 70 * '-')

grade=input("Input the grade: ")

def calculate_grade(grade):
    if grade=='E':
        return "Excellent"
    if grade=='V':
        return "Very Good"
    if grade=='G':
        return "Good"
    if grade=='A':
        return "Average"
    if grade=='F':
        return "Fail"
    
print("You have chosen: ", calculate_grade(grade))
    