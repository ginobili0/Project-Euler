def isPrime(n):
    if n <= 1: return False
    for i in xrange(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

count = 0
x = 0
while count < 10001:
    x += 1
    if isPrime(x): count += 1

print x