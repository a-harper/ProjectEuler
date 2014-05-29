"""Which starting number, under one million, produces the longest chain?"""

def chain_list(n, count=1):
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
    return(count)

longest = [0,0]
for x in range(1000000):
    c = chain_list(x)
    if c > longest[0]:
        longest[0] = c
        longest[1] = x
print longest
#print chain_list(837799)