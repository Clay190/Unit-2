#Clay Kynor
#9/13/17
#gradeCalculator.py - Calculates your letter grade

grade = float(input("Enter your grade "))
if grade>=90:
    print("You earned an A! ")
elif grade>=80:
    print("You have a B ")
elif grade>=70:
    print("You have a C ")
elif grade>=60:
    print("You have a D ")
else:
    print("You have failed! ")
    