# Palindrome Checker: Check if a given string is a palindrome.
# Exercise of string slicing

user_input = input("Enter the word: ").lower()

if user_input == user_input[::-1]:
    print("The word is a Palindrome")

else:
    print("The word is not a Palindrome")
