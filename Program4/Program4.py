#
# Explain what this program does
#

letter = "a"
for _ in range(0, 4):
    if letter == "a":
        letter = "c"
    elif letter == "b":
        letter = "g"
    elif letter == "c":
        letter = "b"
    elif letter == "d":
        letter = "f"
    elif letter == "e":
        letter = "c"
    elif letter == "f":
        letter = "d"
    elif letter == "g":
        letter = "e"
print(letter)
