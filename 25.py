fibs = [1, 2]

while True:
    fibs.append(fibs[-1] + fibs[-2])
    if len(str((fibs[-1]))) == 1000:
        break

print len(fibs) + 1