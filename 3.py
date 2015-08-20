def isPrime(n):
    if n <= 1: return False
    for i in xrange(2, (n // 2) + 1):
        if n % i == 0:
            return False
    return True

largest = 2
num = 600851475143
prod = 1
x = 2

while prod < num:
    if num % x == 0 and isPrime(x):
        prod *= x
        if largest < x:
            largest = x
    x += 1

print largest

