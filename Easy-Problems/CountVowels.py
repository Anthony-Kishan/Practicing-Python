# Write a function that counts the number of vowels in a given string.

user_string = input("Enter a word: ")

def count_Vowel(word):
    vowels = "aeiouAEIOU"
    vowel_counter = 0
    
    for vowel in word:
        if vowel in vowels:
            vowel_counter += 1

    if vowel_counter == 0:
        print("The given word has no vowels")

    print(vowel_counter)

count_Vowel(user_string)