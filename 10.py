def isPrime(n):
    if n <= 1:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    w = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

total = 0
i = 0
while i < 2000000:
    if isPrime(i):
        total += i
    i += 1

print total