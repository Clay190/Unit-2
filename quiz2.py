#Clay Kynor
#9/25/17
#quiz2.py - my quiz

num1 = float(input("Please enter a number: "))
num2 = float(input("Please enter a second number: "))
if num1>num2:
    print("The first number is bigger")
    if num1%3==0 and num2%3==0:
        print("Both numbers are divisible by 3")
        prod1 = int(input("What is the product of your numbers?"))
        if (num1*num2):
            print("Correct")
