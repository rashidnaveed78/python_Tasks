
import random

number = random.randint(1, 100)

print("Guess a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Try again, Too low!")

    elif guess > number:
        print("Try again, Too high!")

    else:
        print("Congratulations! You got the number!.")
        break
