print("=" * 45)
print("        DAY 15 - DICTIONARY IN PYTHON")
print("=" * 45)

# Creating a Dictionary
student = {
    "Name": "Pranjal",
    "Age": 20,
    "Course": "AI & Data Science",
    "CGPA": 8.64
}

# Display Dictionary
print("\nStudent Details:")
print(student)

# Access Dictionary Values
print("\nAccessing Values:")
print("Name   :", student["Name"])
print("Course :", student["Course"])

# Add a New Key
student["College"] = "Sanjivani University"

# Update an Existing Value
student["CGPA"] = 8.75

# Remove a Key
del student["Age"]

# Display Updated Dictionary
print("\nUpdated Student Details:")
print(student)

# Loop Through Dictionary
print("\nDictionary Items:")
for key, value in student.items():
    print(f"{key} : {value}")

# Check if Key Exists
if "Name" in student:
    print("\nThe key 'Name' exists in the dictionary.")

# Dictionary Length
print("\nTotal Keys:", len(student))

print("\nProgram Completed Successfully!")
