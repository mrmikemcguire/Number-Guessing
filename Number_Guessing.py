import random

name = input("\nWhat is your name?  ")
print("Hello, " + name + "!\n")

still_guessing = True
secret_number = random.randrange(1, 5, 1)

while(still_guessing):
    guess = int(input("Choose a a number between 1 and 5   "))
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("You got it!\n")
        still_guessing = False