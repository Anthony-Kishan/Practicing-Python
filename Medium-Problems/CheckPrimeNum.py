# Write a function to check if a number is prime.

user_num = int(input("Enter a number: "))

def CheckPrimeNumber(num):
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                print("The number is not a Prime Number.")
                break
        else:
            print("The number is a Prime Number.")
    else:
        print("1 is not")        
CheckPrimeNumber(user_num)