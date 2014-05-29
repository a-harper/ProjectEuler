__author__ = 'harpera'

"""Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

def sumsquares(top):
    total = 0
    for x in range(1, top+1):
        total += x**2
    return total
def squaresums(top):
    total = 0
    for x in range(1, top+1):
        total += x
    total = total**2
    return total

print squaresums(100) - sumsquares(100)