
import utils

# BMI Calculator
print(utils.calculate_bmi(70, 1.75))

# KM to Miles
print(utils.km_to_miles(10))

# Miles to KM
print(utils.miles_to_km(6.2))

# Celsius to Fahrenheit
print(utils.celsius_to_fahrenheit(25))

# Fahrenheit to Celsius
print(utils.fahrenheit_to_celsius(98.6))

# Calculator
print(utils.calculator(20, 5, "+"))
print(utils.calculator(20, 5, "-"))
print(utils.calculator(45, 5, "*"))
print(utils.calculator(89, 5, "/"))

# FizzBuzz
utils.fizz_buzz(17)

# Multiplication Table
utils.multiplication_table(7)

# Number Guessing Game
utils.number_guessing_game()

# Word Count
text = """Maybe you've forgotten something.
I'm Ben Tennyson — wielder of the most powerful weapon in the universe.
I stopped the Highbreed Invasion. I defeated Vilgax in hand-to-hand combat.
And I've beaten the Forever Knights more times than I can even remember!
So here is my deal:
You let these prisoners go, and you walk away.
Because if you don't... I won't hold back next time."""

print(utils.word_count(text))
