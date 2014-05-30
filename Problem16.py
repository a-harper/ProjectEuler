__author__ = 'harpera'

"""What is the sum of the digits of the number 2^1000?"""
total = 0
num = str(2**1000)
digits = map(int, num)
print digits
print sum(digits)

