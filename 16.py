num = 2 ** 1000
digits = list(str(num))
total = 0
for digit in digits:
    total += int(digit)

print total