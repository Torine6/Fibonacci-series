import math


def perfect_square(x):
    num = int(math.sqrt(x))
    return num * num == x


number = int(input('Enter the number: '))
result1 = 5 * (number * number) + 4
result2 = 5 * (number * number) - 4

if perfect_square(result1) or perfect_square(result2):
    print(number, ' is a Fibonacci number.')
else:
    print(number, ' is not a Fibonacci number.')

