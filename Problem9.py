__author__ = 'harpera'
"""
a^2 + b^2 = c^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc"""

for i in range(1, 1000):
    for j in range (1, 1000-i):
        k = 1000 - i - j
        if i**2 + j**2 == k**2:
            print i*j*k