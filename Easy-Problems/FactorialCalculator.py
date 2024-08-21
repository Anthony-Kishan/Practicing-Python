# Write a function that returns the factorial of a given number

num = int(input("Enter a number to find Factorial: "))

def factorial(num):
    for i in range(1, num):
        num *= i

    return num

print(factorial(num))