n = 20
arr = range(11, 21)

i = 0
while i < 10:
    if n % arr[i] != 0:
        n += 20
        i = 0
    else:
        i += 1

print n