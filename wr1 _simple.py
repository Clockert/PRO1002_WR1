# PRO1002 - Backend Essentials
# Work Requirement 1 - Python Practice Exercises
# Student: Charlotte Iselin Lockert


# ============================================================================
# Exercise 1: Greeting and Age Check
# ============================================================================
print("=== Exercise 1: Greeting and Age Check ===")

name = input("Please enter your name: ")
age_input = input("Please enter your age: ")
age = int(age_input)

if age >= 18:
    print(f"Hello {name}! You can enter.")
else:
    print(f"Sorry {name}, you're too young to enter.")

print()

# ============================================================================
# Exercise 2: Number List Processor
# ============================================================================
print("=== Exercise 2: Number List Processor ===")

n_input = input("Enter a number (how many numbers to create): ")
n = int(n_input)

# Create list of numbers from 1 to n
numbers = []
for i in range(1, n + 1):
    numbers.append(i)

print(f"Numbers from 1 to {n}: {numbers}")

if n > 5:
    print("Your list is long!")
else:
    print("Your list is short!")

print()

# ============================================================================
# Exercise 3: Sum of User Inputs
# ============================================================================
print("=== Exercise 3: Sum of User Inputs ===")

print("I'll help you find out if the sum of three numbers is even or odd!")
num1_input = input("Enter the first number: ")
num2_input = input("Enter the second number: ")
num3_input = input("Enter the third number: ")

# Convert to integers
num1 = int(num1_input)
num2 = int(num2_input)
num3 = int(num3_input)

# Store in list and calculate total
numbers = [num1, num2, num3]
print(f"Your numbers: {numbers}")

total = num1 + num2 + num3
print(f"Total: {total}")

# Check if even or odd
if total % 2 == 0:
    print("Your sum is even!")
else:
    print("Your sum is odd!")

print()

# ============================================================================
# Exercise 4: Fruit Basket
# ============================================================================
print("=== Exercise 4: Fruit Basket ===")

# Create fruit inventory
fruit_basket = {
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "grape": 15,
    "strawberry": 3
}

fruit_name = input("What fruit would you like? ").lower()

if fruit_name in fruit_basket:
    quantity = fruit_basket[fruit_name]
    print(f"We have {quantity} {fruit_name}s available!")
    
    # Print each letter of the fruit name
    print("Letters in the fruit name:")
    for letter in fruit_name:
        print(letter)
else:
    print("We don't have that fruit.")

print()

# ============================================================================
# Exercise 5: Temperature Converter
# ============================================================================
print("=== Exercise 5: Temperature Converter ===")

celsius_input = input("Enter temperature in Celsius: ")
celsius = float(celsius_input)

# Convert to Fahrenheit
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C is {fahrenheit}°F")

if fahrenheit > 80:
    print("It's hot!")
else:
    print("It's not too hot.")

# Store both temperatures
temperatures = [celsius, fahrenheit]
print(f"Temperatures: {temperatures}")

print()

# ============================================================================
# Exercise 6: Menu Selection
# ============================================================================
print("=== Exercise 6: Menu Selection ===")

# Create menu with prices
menu = {
    "coffee": 30,
    "tea": 20,
    "juice": 25,
    "sandwich": 45,
    "cake": 35
}

order = input("What would you like to order? (coffee, tea, juice, sandwich, cake): ").lower()

# Check if item exists and show price
if order in menu:
    price = menu[order]
    print(f"The price for {order} is {price} kr.")
else:
    print("Item not found.")

# Display full menu
print("\n--- Full Menu ---")
for item, price in menu.items():
    print(f"{item}: {price} kr")

print()

# ============================================================================
# Exercise 7: Number Analyzer
# ============================================================================
print("=== Exercise 7: Number Analyzer ===")

numbers_input = input("Enter numbers separated by spaces (e.g., '10 5 20'): ")
number_strings = numbers_input.split()

# Convert strings to integers
numbers = [int(num_str) for num_str in number_strings]
print(f"Your numbers: {numbers}")

print("Analyzing your numbers...")

# Find min, max, and average manually
smallest = numbers[0]
largest = numbers[0]
total = 0

for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
    total += num

average = total / len(numbers)

print("--- Analysis Results ---")
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
print(f"Average: {average:.2f}")

if average > 10:
    print("Average is high")
else:
    print("Average is low")

print()

# ============================================================================
# Exercise 8: Letter Counter
# ============================================================================
print("=== Exercise 8: Letter Counter ===")

word_input = input("Enter a word: ")
word = word_input.lower()

print(f"Analyzing the word: '{word}'")

# Count each letter
letter_counts = {}
for letter in word:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

print(f"Letter counts: {letter_counts}")

word_length = len(word)
print(f"Word length: {word_length} letters")

if word_length > 5:
    print("That's a long word!")
else:
    print("That's a short word!")

print()

# ============================================================================
# Exercise 9: Guessing Game
# ============================================================================
print("=== Exercise 9: Guessing Game ===")

secret_number = 7
guesses = []

print("I'm thinking of a number between 1 and 10...")

while True:
    guess_input = input("What's your guess? ")
    guess = int(guess_input)
    guesses.append(guess)
    
    if guess == secret_number:
        print("You got it!")
        break
    else:
        print("Try again!")

print(f"All your guesses: {guesses}")
print(f"It took you {len(guesses)} tries to guess the number!")

print()

# ============================================================================
# Exercise 10: Shopping List Manager
# ============================================================================
print("=== Exercise 10: Shopping List Manager ===")

shopping_list = []

while True:
    item = input("Enter an item to add (or 'done' to finish): ").lower()
    
    if item == "done":
        break
    
    shopping_list.append(item)
    print(f"Added '{item}' to your shopping list.")

print(f"\nYour complete shopping list: {shopping_list}")

if len(shopping_list) > 3:
    print("You have a lot of items!")
else:
    print("You have a short list.")

print("\n=== All exercises completed! ===")