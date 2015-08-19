def num_factors(n):
    div = 1
    x = 0
    while n > 1:
        c = 1
        while not n % prime(x):
            c = c + 1
            n = n / prime(x)
        x = x + 1
        div = div * c
    return div

for i in xrange(1, 1000000000):
    if num_factors(i) > 500:
        print i
        break