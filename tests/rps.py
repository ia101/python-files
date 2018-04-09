import random

a = ["R", "P", "S"]
playAgain = "Y"

while playAgain == "Y":

    playerM = input("Choose R (rock), P(Peper) or S(Scissors): ")

    cpuM = random.choice(a)
    print("CPU: " + cpuM)

    if playerM == cpuM:
        print("Draw!!")

    if playerM == "R" and cpuM == "S":
        print("You Won!!")

    if playerM == "R" and cpuM == "P":
        print("You Lose!!")

    if playerM == "P" and cpuM == "S":
        print("You Lose!!")

    if playerM == "P" and cpuM == "R":
        print("You Won!!")

    if playerM == "S" and cpuM == "R":
        print("You Lose!!")

    if playerM == "S" and cpuM == "P":
        print("You Won!!")



    # playAgain = input("Play more? (Y,N): ")