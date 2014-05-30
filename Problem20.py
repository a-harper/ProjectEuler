__author__ = 'harpera'
"""Find the sum of the digits in the number 100!"""

def factorial(n):
    return reduce(lambda x,y: x*y, range(1,n+1,1))

def sum_digits(n):
    return sum([int(i) for i in str(n)])

print sum_digits(factorial(100))