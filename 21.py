def divsums(n):
    result = 0
    l = n / 2 if n % 2 == 0 else (n + 1) / 2
    for i in xrange(1, l + 1):
        if n % i == 0:
            result += i
    return result

amicableNums = 0

for a in xrange(1, 10000):
    b = divsums(a)
    if divsums(b) == a and b != a:
        amicableNums = amicableNums + a + b

print amicableNums / 2



