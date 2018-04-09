import random

num = random.randint(1, 20)
guss = 0
userNum = int(input("guess a number from 1 to 20: "))
while guss == 0:

    if userNum == num:
        print("You guessed it :) ")
        guss = 1
        break
    elif userNum > num:
        print("it's too high ")
    elif userNum < num:
        print("it's too low ")

    userNum = int(input("guess again: "))

