print("=" * 50)
print("        DAY 18 : TUPLES IN PYTHON")
print("=" * 50)

# Creating a tuple
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

print("\nTuple:")
print(fruits)

# Length
print("\nTotal Fruits:", len(fruits))

# Access elements
print("\nFirst Fruit :", fruits[0])
print("Last Fruit  :", fruits[-1])

# Membership test
fruit = input("\nEnter a fruit name to search: ")

if fruit in fruits:
    print(f"{fruit} is available in the tuple.")
else:
    print(f"{fruit} is not available in the tuple.")

print("\nIterating through the tuple:")
for item in fruits:
    print(item)

print("\nProgram Completed Successfully!")
