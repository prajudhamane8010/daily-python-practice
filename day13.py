# Day 13 - Check if Two Strings are Anagrams
# Date: 2026-07-22

print("==== Day 13 : Check if Two Strings are Anagrams ====\n")

str1 = input("Enter the first string: ").lower().replace(" ", "")
str2 = input("Enter the second string: ").lower().replace(" ", "")

if sorted(str1) == sorted(str2):
    print(f"\n'{str1}' and '{str2}' are Anagrams.")
else:
    print(f"\n'{str1}' and '{str2}' are NOT Anagrams.")

print("\nProgram Completed Successfully!")
