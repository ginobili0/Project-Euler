def divsums(n):
    result = 0
    for i in xrange(1, n // 2 + 1):
        if n % i == 0:
            result += i
    return result

amicableNums = 0

for a in xrange(1, 10000):
    b = divsums(a)
    if divsums(b) == a and b != a:
        amicableNums += a

print amicableNums



