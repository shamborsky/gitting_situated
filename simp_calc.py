print("Hello World Boye")

num1 = input("enter first number: ")
num2 = input("enter second number: ")
operator = input("whatcha wanna do? \nAdd\nSubtract\nMultiply\nDivide\n\n")

if operator == "Add":
    suem = int(num1) + int(num2)
    print("Your total is " + str(suem))
elif operator == "Subtract":
    suem = int(num1) - int(num2)
    print("Your total is " + str(suem))
elif operator == "Multiply":
    suem = int(num1) * int(num2)
    print("Your total is " + str(suem))
elif operator == "Divide":
    suem = int(num1) / int(num2)
    print("Your total is " + str(suem))
else:
    print("Please pick from one of the options")

print("\nHave a nice day!")