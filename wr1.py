# PRO1002 - Backend Essentials
# Work Requirement 1 - Python Practice Exercises
# Student: Charlotte Iselin Lockert


# NOTE: In professional code, I would not normally include this level of detailed commenting.
# However, for learning purposes, I've added extensive WHY and HOW explanations to demonstrate
# my understanding of Python concepts, design decisions, and execution mechanics.
# These detailed comments were developed with AI assistance after writing the working code,
# to enhance my own learning experience and hopefully make the peer review process more
# educational for my classmates as well. 
# ============================================================================
# Exercise 1: Greeting and Age Check
# ============================================================================
print("=== Exercise 1: Greeting and Age Check ===")

# Prompt the user to enter their name and age
# WHY: We need user input to personalize the greeting and make the age-based decision
# HOW: input() function displays the prompt text and waits for user to type and press Enter
name = input("Please enter your name: ")
age_input = input("Please enter your age: ")

# Store these in variables and convert the age input to an integer
# WHY: input() always returns a string, but we need an integer for numerical comparison
# HOW: int() parses the string character by character and converts to integer value
age = int(age_input)

# Use a conditional: If the user is 18 or older, print greeting; otherwise say they're too young
# WHY: We use >= instead of == because many ages qualify (18, 19, 20, etc.)
# HOW: Python evaluates (age >= 18) returning True/False, then executes appropriate block
if age >= 18:
    print(f"Hello {name}! You can enter.")
else:
    print(f"Sorry {name}, you're too young to enter.")

print()

# ============================================================================
# Exercise 2: Number List Processor
# ============================================================================
print("=== Exercise 2: Number List Processor ===")

# Ask the user for a number n (integer)
# WHY: We need a limit to know how many numbers to generate in our list
# HOW: input() gets string, int() converts it to integer for use in range()
number_input = input("Enter a number (how many numbers to create): ")
n = int(number_input)

# Create a list of numbers from 1 up to n using a for loop and range()
# WHY: range() is the most efficient way to generate sequences of numbers
# HOW: range(1, n+1) creates sequence from 1 to n (inclusive), list() converts to list
numbers = []
for i in range(1, n + 1):
    numbers.append(i)

# Print the list
# HOW: print() automatically formats the list with square brackets and commas
print(f"Numbers from 1 to {n}: {numbers}")

# If n is greater than 5, print message that list is long; otherwise say it's short
# WHY: This demonstrates conditional logic based on calculated values
# HOW: Python compares n with 5, executes appropriate branch based on True/False result
if n > 5:
    print("Your list is long!")
else:
    print("Your list is short!")

print()

# ============================================================================
# Exercise 3: Sum of User Inputs
# ============================================================================
print("=== Exercise 3: Sum of User Inputs ===")

# Ask the user for three numbers (as strings), convert them to integers
# WHY: We need three separate values to demonstrate variables, lists, and arithmetic
# HOW: Each input() call waits for user input, int() converts string to integer
print("I'll help you find out if the sum of three numbers is even or odd!")
num1_input = input("Enter the first number: ")
num2_input = input("Enter the second number: ")
num3_input = input("Enter the third number: ")

num1 = int(num1_input)
num2 = int(num2_input)
num3 = int(num3_input)

# Use a list to hold these three numbers and print the list
# WHY: Lists group related data and demonstrate collection usage
# HOW: [num1, num2, num3] creates list object containing the three integer values
numbers = [num1, num2, num3]
print(f"Your numbers: {numbers}")

# Add them up and print the total
# WHY: Direct addition is clear and shows understanding of arithmetic operations
# HOW: Python performs addition left to right: (num1 + num2) + num3
total = num1 + num2 + num3
print(f"Total: {total}")

# If the total is even, print "Your sum is even!", else print "Your sum is odd!"
# WHY: Modulo operator is the standard way to check divisibility by 2
# HOW: % operator returns remainder after division; remainder 0 means even number
if total % 2 == 0:
    print("Your sum is even!")
else:
    print("Your sum is odd!")

print()

# ============================================================================
# Exercise 4: Fruit Basket
# ============================================================================
print("=== Exercise 4: Fruit Basket ===")

# Create a dictionary to store fruit names as keys and their quantities as values
# WHY: Dictionaries provide O(1) lookup time for key-value associations
# HOW: {} creates hash table where each key maps directly to its value
fruit_basket = {
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "grape": 15,
    "strawberry": 3
}

# Prompt the user for a fruit name
# WHY: .lower() makes input case-insensitive for better user experience
# HOW: .lower() creates new string with all characters converted to lowercase
fruit_name = input("What fruit would you like? ").lower()

# If it's in the dictionary, print how many are available
# WHY: 'in' operator prevents KeyError exceptions with safe key checking
# HOW: 'in' uses hash table to quickly check key existence without searching all keys
if fruit_name in fruit_basket:
    quantity = fruit_basket[fruit_name]
    print(f"We have {quantity} {fruit_name}s available!")
    
    # Use a loop to print each letter of the fruit's name on a new line
    # WHY: Strings are iterable sequences, demonstrating that strings behave like lists
    # HOW: for loop automatically gets each character and assigns it to 'letter' variable
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

# Ask the user for a temperature in Celsius (string, convert to float)
# WHY: Temperature can have decimal places, so float is more appropriate than int
# HOW: float() parses string and converts to floating-point number with decimal precision
celsius_input = input("Enter temperature in Celsius: ")
celsius = float(celsius_input)

# Convert it to Fahrenheit and print the result
# WHY: Standard temperature conversion formula: F = C * 9/5 + 32
# HOW: Python performs arithmetic operations in order: multiplication, division, addition
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C is {fahrenheit}°F")

# If Fahrenheit > 80, print "It's hot!" else print "It's not too hot."
# WHY: 80°F is a reasonable threshold for demonstrating conditional logic
# HOW: Python compares fahrenheit value with 80, executes appropriate branch
if fahrenheit > 80:
    print("It's hot!")
else:
    print("It's not too hot.")

# Add both Celsius and Fahrenheit values to a list, then print the list
# WHY: Demonstrates storing calculated results in a collection
# HOW: List stores both temperature values, allowing easy display and future processing
temperatures = [celsius, fahrenheit]
print(f"Temperatures: {temperatures}")

print()

# ============================================================================
# Exercise 6: Menu Selection
# ============================================================================
print("=== Exercise 6: Menu Selection ===")

# Create a dictionary that maps menu item names to their prices
# WHY: Dictionary is ideal for associating menu items with prices for quick lookup
# HOW: Each key-value pair creates a mapping stored in the hash table structure
menu = {
    "coffee": 30,
    "tea": 20,
    "juice": 25,
    "sandwich": 45,
    "cake": 35
}

# Ask the user what they'd like to order
# WHY: .lower() ensures case-insensitive matching for better user experience
# HOW: input() gets string, .lower() transforms each character to lowercase
order = input("What would you like to order? (coffee, tea, juice, sandwich, cake): ").lower()

# If the item is in the dictionary, print its price. Otherwise, print "Item not found."
# WHY: Defensive programming - always check key existence before accessing value
# HOW: 'in' operator checks hash table for key, preventing KeyError exceptions
if order in menu:
    price = menu[order]
    print(f"The price for {order} is {price} kr.")
else:
    print("Item not found.")

# Use a loop to print all items and their prices after the user's query
# WHY: .items() gets both keys and values simultaneously, more efficient than separate lookups
# HOW: .items() returns (key, value) tuples, Python unpacks them into item and price variables
print("\n--- Full Menu ---")
for item, price in menu.items():
    print(f"{item}: {price} kr")

print()

# ============================================================================
# Exercise 7: Number Analyzer
# ============================================================================
print("=== Exercise 7: Number Analyzer ===")

# Ask the user for a series of numbers separated by spaces
# WHY: Space-separated input is user-friendly and demonstrates string processing
# HOW: input() gets entire string, split() divides it at spaces into list of strings
numbers_input = input("Enter numbers separated by spaces (e.g., '10 5 20'): ")
number_strings = numbers_input.split()

# Split the input into a list of strings, convert each to an integer
# WHY: split() creates strings, but we need integers for mathematical operations
# HOW: List comprehension iterates through strings, int() converts each to integer
numbers = [int(num_str) for num_str in number_strings]
print(f"Your numbers: {numbers}")

# Using a loop, find the smallest, largest, and average values
# WHY: Manual calculation demonstrates loop usage and mathematical operations
# HOW: Loop through list, comparing each value to track min/max, sum for average
smallest = numbers[0]  # Start with first number
largest = numbers[0]
total = 0

for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
    total += num

# HOW: Division gives average, len() counts list items without manual counting
average = total / len(numbers)

print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
print(f"Average: {average}")

# Use an if statement: if the average is greater than 10, print "Average is high"
# WHY: Demonstrates conditional logic on calculated values
# HOW: Python compares average (float) with 10 (int), automatic type coercion occurs
if average > 10:
    print("Average is high")
else:
    print("Average is low")

print()

# ============================================================================
# Exercise 8: Letter Counter
# ============================================================================
print("=== Exercise 8: Letter Counter ===")

# Prompt the user for a word (string)
# WHY: We need text input to demonstrate string processing and character counting
# HOW: input() captures whatever the user types as a string
word_input = input("Enter a word: ")

# Convert the word to lowercase
# WHY: Case-insensitive counting treats 'A' and 'a' as the same letter
# HOW: .lower() creates new string with all uppercase letters converted to lowercase
word = word_input.lower()

print(f"Analyzing the word: '{word}'")

# Using a loop, count how many times each letter appears and store in dictionary
# WHY: Dictionary is perfect for mapping letters to their counts
# HOW: Loop through each character, use dictionary to track count for each letter
letter_counts = {}
for letter in word:
    # HOW: .get() returns current count or 0 if letter not seen before, then add 1
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

# Print the dictionary
# HOW: print() displays dictionary with curly braces showing key: value pairs
print(f"Letter counts: {letter_counts}")

# If the word length is more than 5 letters, print "That's a long word!"
# WHY: len() gives character count, demonstrating conditional logic on string properties
# HOW: len() counts each character in the string and returns the total as integer
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

# Set a secret number in a variable
# WHY: Fixed number for simplicity, could use random.randint() for variety
# HOW: Integer literal 7 is stored directly in memory for comparison
secret_number = 7

# Keep track of their guesses in a list
# WHY: List maintains order of guesses and can grow dynamically
# HOW: [] creates empty list object, append() will add items to the end
guesses = []

print("I'm thinking of a number between 1 and 10...")

# Use a while loop to ask the user to guess the number
# WHY: while True creates infinite loop since we don't know how many guesses needed
# HOW: Loop continues indefinitely until 'break' statement explicitly exits
while True:
    guess_input = input("What's your guess? ")
    
    # Convert their input to an integer
    # WHY: input() returns string, but we need integer for numerical comparison
    # HOW: int() parses string digits and creates integer value for comparison
    guess = int(guess_input)
    
    # HOW: append() adds the new guess to end of list, maintaining chronological order
    guesses.append(guess)
    
    # If they guess correctly, print "You got it!" and break out of the loop
    # WHY: break provides clean exit from infinite loop when condition is met
    # HOW: == operator compares two integers, returns True if equal, False otherwise
    if guess == secret_number:
        print("You got it!")
        break
    else:
        print("Try again!")

# After they guess correctly, print the list of all their guesses
# WHY: Shows complete game history and demonstrates list usage for tracking
# HOW: print() formats list automatically, len() counts items without manual iteration
print(f"All your guesses: {guesses}")
print(f"It took you {len(guesses)} tries to guess the number!")

print()

# ============================================================================
# Exercise 10: Shopping List Manager
# ============================================================================
print("=== Exercise 10: Shopping List Manager ===")

# Start with an empty list called shopping_list
# WHY: Empty list can grow dynamically as user adds items
# HOW: [] creates empty list object in memory, ready to accept new items
shopping_list = []

# Use a while loop to repeatedly ask the user to enter an item
# WHY: while True allows indefinite input until user decides to stop
# HOW: Infinite loop continues until user types "done" and we break out
while True:
    # Each time the user enters an item, add it to the list
    # WHY: We need to capture user input and check for the exit condition
    # HOW: input() waits for user input, .lower() ensures case-insensitive comparison
    item = input("Enter an item to add (or 'done' to finish): ").lower()
    
    # If they type "done", exit the loop
    # WHY: Provides clear exit condition that user can control
    # HOW: String comparison checks if user input matches "done" exactly
    if item == "done":
        break
    
    # HOW: append() adds the item string to the end of the list
    shopping_list.append(item)
    print(f"Added '{item}' to your shopping list.")

# When done, print the full list
# HOW: print() displays the complete list with square brackets and comma separation
print(f"\nYour complete shopping list: {shopping_list}")

# If the list has more than 3 items, print message; otherwise print different message
# WHY: Demonstrates conditional logic based on collection size
# HOW: len() counts items in list, comparison operator determines which message to show
if len(shopping_list) > 3:
    print("You have a lot of items!")
else:
    print("You have a short list.")

print("\n=== All exercises completed! ===")