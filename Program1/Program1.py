#
# Explain what this program does
#

while True:
    numberOne = int(input("Number? "))
    action = input("Action (+, -, / or *)? ")
    numberTwo = int(input("Number? "))
    if action == "+":
        print()
        print(numberOne + numberTwo)
        print()
    elif action == "-":
        print()
        print(numberOne - numberTwo)
        print()
    elif action == "/":
        print()
        print(numberOne / numberTwo)
        print()
    elif action == "*":
        print()
        print(numberOne * numberTwo)
        print()
    else:
        print()
        print("Invalid action! Supported actions are +, -, / and *! Please retry!")
        print()
