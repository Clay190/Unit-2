#Clay Kynor
#9/14/17
#compoundConditionalDemo.py - using and/or

num = float(input("Please enter a number: "))

if num>0 and num%7 == 0:
    print("Your number is positive and divisible by 7")
elif num>0:
    print("Your number is postitive and not divisible by 7")
elif num<0 and num%7 == 0:
    print("Your number is negative and divisible by 7")
elif num<0:
    print("Your number is negative and not divisible by 7")
