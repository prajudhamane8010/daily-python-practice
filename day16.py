print("=" * 45)
print("        DAY 16 - FUNCTIONS IN PYTHON")
print("=" * 45)

# Function without parameters
def welcome():
    print("\nWelcome to Python Programming!")

# Function with parameters
def greet(name):
    print(f"Hello, {name}! Welcome to Day 16.")

# Function with return value
def add(a, b):
    return a + b

# Function to find square
def square(num):
    return num * num

# Calling functions
welcome()

greet("Pranjal")

result = add(15, 25)
print("\nAddition:", result)

number = 8
print(f"Square of {number}:", square(number))

print("\nProgram Completed Successfully!")
