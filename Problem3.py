__author__ = 'harpera'
import math
"""What is the largest prime factor of the number 600851475143 ?"""

target = 600851475143

i = 2
while i * i < target:
     while target % i == 0:
         target = target / i
     i += 1

print (target)