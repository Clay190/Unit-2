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
        if (num1*num2)==prod1:
            print("Correct")
        else:
            print("Incorrect")
    elif num1%3==0:
        print("Only the first number is divisible by 3")
        prod2 = int(input("What is the product of your numbers?"))
        if (num1*num2)==prod2:
            print("Correct")
        else:
            print("Incorrect")
    elif num2%3==0:
        print("Only the second number is divisible by 3")
        prod3 = int(input("What is the product of your numbers?"))
        if (num1*num2)==prod3:
            print("Correct")
        else:
            print("Incorrect")
    else:
        print("None of you numbers are divisible by 3")
        prod4 = int(input("What is the product of your numbers?"))
        if (num1*num2)==prod4:
            print("Correct")
        else:
            print("Incorrect")
elif num1<num2:
    print("The second number is bigger")
    if num1%3==0 and num2%3==0:
        print("Both numbers are divisible by 3")
        pro1 = int(input("What is the product of your numbers?"))
        if (num1*num2)==pro1:
            print("Correct")
        else:
            print("Incorrect")
    elif num1%3==0:
        print("Only the first number is divisible by 3")
        pro2 = int(input("What is the product of your numbers?"))
        if (num1*num2)==pro2:
            print("Correct")
        else:
            print("Incorrect")
    elif num2%3==0:
        print("Only the second number is divisible by 3")
        pro3 = int(input("What is the product of your numbers?"))
        if (num1*num2)==pro3:
            print("Correct")
        else:
            print("Incorrect")
    else:
        print("None of you numbers are divisible by 3")
        pro4 = int(input("What is the product of your numbers?"))
        if (num1*num2)==pro4:
            print("Correct")
        else:
            print("Incorrect")
else:
    print("Your numbers are the same")
    if num1%3==0:
        print("Both your numbers are divisible by 3")
        product1 = int(input("What is the product of your numbers?"))
        if num1**2==product1:
            print("Correct")
        else:
            print("False")
    else:
        print("Your numbers are not divisible by 3")
        product2 = int(input("What is the product of your numbers?"))
        if num1**2==product2:
            print("Correct")
        else:
            print("False")
