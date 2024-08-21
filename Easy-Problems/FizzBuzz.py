'''
FizzBuzz: Print numbers from 1 to 100.
- For multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz".
- For numbers which are multiples of both 3 and 5, print "FizzBuzz".
'''

for i in range(1, 101):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 and 5:
        print('FizzBuzz')
    else:
        print(i)
