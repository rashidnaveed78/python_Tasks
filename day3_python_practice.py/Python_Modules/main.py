
import random

# BMI Calculator
def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)


# KM to Miles
def km_to_miles(km):
    return round(km * 0.621371, 2)


# Miles to KM
def miles_to_km(miles):
    return round(miles * 1.60934, 2)


# Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return round((celsius * 9/5) + 32, 2)


# Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)


# Calculator
def calculator(a, b, operator):

    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    else:
        return "Invalid operator"


# FizzBuzz
def fizz_buzz(number):

    for i in range(1, number + 1):

        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

        elif i % 3 == 0:
            print("Fizz")

        elif i % 5 == 0:
            print("Buzz")

        else:
            print(i)


# Multiplication Table
def multiplication_table(number):

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


# Number Guessing Game
def number_guessing_game():

    number = random.randint(1, 100)

    print("\nGuess a number between 1 and 100")

    while True:

        guess = int(input("Enter your guess: "))

        if guess < number:
            print("Too low! Try again.")

        elif guess > number:
            print("Too high! Try again.")

        else:
            print("Congratulations! You guessed it.")
            break


# Word Count
def word_count(text):

    words = text.split()

    return len(words)
