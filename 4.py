n = 0

for a in xrange(999, 100, -1):
    for b in xrange(a, 100, -1):
        x = a * b
        if x > n and str(x) == str(x)[::-1]:
                n = x

print n
