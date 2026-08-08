print("=" * 50)
print("        DAY 23 - FILE HANDLING")
print("=" * 50)

filename = "student.txt"

# Write data to the file
with open(filename, "w") as file:
    file.write("Name: Pranjal\n")
    file.write("Course: B.Tech AI & Data Science\n")
    file.write("Subject: Python\n")
    file.write("Day: 23\n")

print("\nData written successfully!")

# Read data from the file
print("\n--- File Content ---")

with open(filename, "r") as file:
    content = file.read()
    print(content)

# Add more data
with open(filename, "a") as file:
    file.write("Status: Learning Python\n")

print("New data added successfully!")

print("\nProgram Completed Successfully!")
