__author__ = 'harpera'
"""By considering the terms in the Fibonacci sequence whose values do not exceed four million,
    find the sum of the even-valued terms."""
phi = (1 + 5**0.5) / 2
def fib(n):
    return int(round((phi**n - (1-phi)**n) / 5**0.5))
memo = {0:0, 1:1}
fiblist = []
ceiling = 4000000
x = 0
thefib = 0
while thefib < ceiling:
    thefib = fib(x)
    fiblist.append(thefib)
    x += 1
# print fiblist
answer = sum(filter(lambda x: x % 2 == 0, fiblist))
print answer