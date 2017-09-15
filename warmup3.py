#Clay Kynor
#9/15/17
#warmup3.py - divisible by 2 and 3

num = int(input("Please enter an integer "))
if num%3 == 0 and num%2 == 0:
    print("Your number is divisible by 2 and 3 ")
elif num%3 == 0:
    print("Your number is divisible by only 3 ")
elif num%2 == 0:
    print("Your number is only divisible by 2 ")
else:
    print("Your number is not divisible by 2 or 3 ")