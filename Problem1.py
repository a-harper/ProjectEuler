__author__ = 'harpera'

result = sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1,1000)))
print(result)