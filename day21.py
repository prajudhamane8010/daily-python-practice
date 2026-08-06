print("=" * 50)
print("        DAY 21 - SIMPLE CALCULATOR")
print("=" * 50)

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("\nChoose Operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("\nEnter your choice (1-4): ")

if choice == "1":
    print("\nResult =", num1 + num2)

elif choice == "2":
    print("\nResult =", num1 - num2)

elif choice == "3":
    print("\nResult =", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("\nResult =", num1 / num2)
    else:
        print("\nError! Division by zero is not allowed.")

else:
    print("\nInvalid Choice!")

print("\nProgram Completed Successfully!")
