__author__ = 'harpera'
"""What is the value of the first triangle number to have over five hundred divisors?"""

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
Found = False
i = 1
triangle = 0
while not Found:
    triangle = 0
    triangle += i
    for j in range(i, 0, -1):
        triangle += i-j
    if len(factors(triangle)) >= 500:
        Found = True
    i += 1
print triangle
print i