# this is a Python fuction that checks whether a number belongs to the Fibonacci sequence or not
# in Fibonnacci sequence each number is the sum of the two preciding numbers
# a number is Fibonacci iff 5n^2+4 or 5n^2-4 is a perfect square
import math

# defining the function and finding square root of the number
def perfect_square(x):
    num = int(math.sqrt(x))
    return num * num == x

# checking whether line 3 is true for the given number
number = int(input('Enter the number: '))
result1 = 5 * (number * number) + 4
result2 = 5 * (number * number) - 4

if perfect_square(result1) or perfect_square(result2):
    print(number, ' is a Fibonacci number.')
else:
    print(number, ' is not a Fibonacci number.')

