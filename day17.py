print("=" * 50)
print("      DAY 17 : LIST COMPREHENSION")
print("=" * 50)

# Input numbers
numbers = list(map(int, input("\nEnter numbers separated by spaces: ").split()))

# Square of numbers
squares = [num ** 2 for num in numbers]

# Even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

# Odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]

print("\nOriginal List :", numbers)
print("Square List   :", squares)
print("Even Numbers  :", even_numbers)
print("Odd Numbers   :", odd_numbers)

print("\nProgram Completed Successfully!")
