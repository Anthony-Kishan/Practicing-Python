# Write a function that reverses a given string.

user_string = input("Enter a String: ")

def ReverseString(text):
    text1 = ""
    for i in text:
        text1 = i + text1
    print(text1)


ReverseString(user_string)