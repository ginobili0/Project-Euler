total = 0

for i in range(2, 354294):
    digsum = 0
    for digit in str(i):
        digsum += int(digit) ** 5
    if digsum == i: total += i

print total