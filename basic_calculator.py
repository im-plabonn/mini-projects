num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
operation = input("What you want to perform(+, -, *, /)? ")
if (operation == "+"):
    print(num1+num2)
elif (operation == "-"):
    print(num1-num2)
elif (operation == "*"):
    print(num1*num2)
elif (operation == "/"):
    print(num1/num2)
else:
    print("Please type correct operation!!!")