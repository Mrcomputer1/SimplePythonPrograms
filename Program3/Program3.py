#
# Explain what this program does
#

answerOne = 20
answer = 0
while not answerOne < 11:
    answerOne = int(input("Please enter a number? "))
    answer = answerOne
if answer == 10:
    for _ in range(0, 10):
        answerOne = answerOne + 1
if answer < 10:
    if answer < 5:
        if answer == 1:
            for _ in range(0, 3):
                answerOne = answerOne * 2
                answerOne = 5
        if answer == 2:
            for _ in range(0, 11):
                answerOne = answerOne + 10
        if answer == 3:
            for _ in range(0, 3):
                answerOne = answerOne + 20
        if answer == 4:
            for _ in range(0, 2):
                answerOne = answerOne * 4
if answerOne == 5:
    for _ in range(0, 9):
        answerOne = answerOne + 3
if answer > 5:
    if answer == 6:
        for _ in range(0, 10):
            answerOne = answerOne + 5
    if answer == 7:
        for _ in range(0, 2):
            answerOne = answerOne * 3
    if answer == 8:
        for _ in range(0, 6):
            answerOne = answerOne * 2
    if answer == 9:
        for _ in range(0, 4):
            answerOne = answerOne + 2
print(answerOne)
