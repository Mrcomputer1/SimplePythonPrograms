#
# Explain what this program does
#

numberOne = int(input("Number? "))
action = input("Action (+, -, / or *)? ")
numberTwo = int(input("Number? "))
if action == "+":
    print()
    print(numberOne, "+", numberTwo, "=", numberOne + numberTwo)
    print()
elif action == "-":
    print()
    print(numberOne, "-", numberTwo, "=", numberOne - numberTwo)
    print()
elif action == "/":
    print()
    print(numberOne, "/", numberTwo, "=", numberOne / numberTwo)
    print()
elif action == "*":
    print()
    print(numberOne, "*", numberTwo, "=", numberOne * numberTwo)
    print()
else:
    print()
    print("Invalid action! Supported actions are +, -, / and *!")
    print()
