
import random

# Multiplication Table Function
def multiplication_table(number: int) -> None:
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


# BMI Calculator Function
def calculate_bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)


# FizzBuzz Function
def fizz_buzz(n: int) -> None:
    """Prints the FizzBuzz sequence from 1 to n."""
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# Calculator Function
def calculator(num1: float, num2: float, operator: str):
    """Performs a basic arithmetic operation."""
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Cannot divide by zero."
        return num1 / num2
    else:
        return "Invalid operator."


# Number Guessing Game
def number_guessing_game() -> None:
    number = random.randint(1, 100)

    while True:
        guess = int(input("Enter your guess: "))

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number.")
            break


# Word Count Function
def word_count(text: str) -> dict:
    counts = {}

    for word in text.split():
        word = word.strip('.,!?";:()[]{}').lower()

        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


# KM to Miles
def km_to_miles(km: float) -> float:
    """Converts kilometers to miles."""
    return km * 0.621371


# Miles to KM
def miles_to_km(miles: float) -> float:
    """Converts miles to kilometers."""
    return miles / 0.621371


# Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius: float) -> float:
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


# Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9
