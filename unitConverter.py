#Clay Kynor
#9/14/17
#unitConverter.py - Converter

while True:
    print("1. Kilometers to Miles")
    print("2. Kilograms to Pounds")
    print("3. Liters to Gallons")
    print("4. Celsius to Fahrenheit")
    print("5. Quit the program")
    num = int(input("Please select a converstion number: "))
    if num%5 == 0:
        break
    elif num%4 == 0:
        celsius = float(input("Enter a degrees in Celsius "))
        print(celsius, "degrees Celsius is", (9/5*celsius+32), "degrees Fahrenheit")
    elif num%3 == 0:
        liters = float(input("Enter the amout of Liters: "))
        print(liters, "in Liters is the same as ", (liters*0.264), "gallons")
    elif num%2 == 0:
        kilo = float(input("Enter the amount of Kilometers: "))
        print(kilo, "in Kilometers is the same as", (kilo*2.2), "in Gallons")
    elif num%1 == 0:
        kilometers = float(input("Enter the amount of Kilometers"))
        print(kilometers, "in Kilometers is the same as", (kilometers*0.62), "in Miles")
    else:
        print("Invalid input")