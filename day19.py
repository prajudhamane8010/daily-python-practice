import random
import string

print("=" * 50)
print("      DAY 19 - PASSWORD GENERATOR")
print("=" * 50)

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password)

print("\nProgram Completed Successfully!")
