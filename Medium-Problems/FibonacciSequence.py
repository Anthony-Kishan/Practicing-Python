# Write a function to return the n-th Fibonacci number.

user_num = int(input("Enter the N-th number: "))

def FibonacciSeries(num):
    a = 0
    b = 1
    if num < 0:
        print("Please enter number greater than 0")
    else:
        if num == 1 or num == 0:
            print(a)
        else:
            print(a, end=" ")
            print(b, end=" ")
            for i in range(2, num):
                c = a + b 
                a = b
                b = c
                print(b, end=" ")
                
FibonacciSeries(user_num)