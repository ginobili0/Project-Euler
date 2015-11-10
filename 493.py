from math import factorial

def choose(n, k):
    return factorial(n)/(factorial(k) * factorial(n - k))

prob = 7 * (1 - float(choose(60, 20)) / choose(70, 20))
print prob