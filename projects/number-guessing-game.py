import random

RandomNumber = random.randrange(1, 500)

while True:
    userInput = int(input("Guess a number between 1 and 500: "))
    if userInput > RandomNumber:
        print("The number is too high!")
    elif userInput < RandomNumber:
        print("The number is too low!")
    else:
        print("Yes, you guessed the right number!")
        break