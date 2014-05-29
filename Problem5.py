__author__ = 'harpera'
"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

i = 1
notfound = True

while notfound:
    remainder = 0
    j = 1
    while remainder == 0 and j < 21:
        remainder += i % j
        j += 1
    if remainder == 0:
        notfound = False
    else: i += 1
print i