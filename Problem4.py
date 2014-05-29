__author__ = 'harpera'
"""A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
    Find the largest palindrome made from the product of two 3-digit numbers."""

def ispalindrome(number):
    string = str(number)
    string2 = string[::-1]
    if string == string2:
        return True
    else: return False

palindromes = []
for i in range(100, 1000):
    for j in range(100, 1000):
        test = i * j
        if ispalindrome(test):
            palindromes.append(test)

print reduce(lambda a,b: a if (a > b) else b, palindromes)
