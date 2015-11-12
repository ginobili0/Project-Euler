maxlen = 1
result = 0
num = 1000

while num > 1:
    rems = []
    num -= 1
    length = 0
    i = 10 ** len(str(num))
    while (i % num not in rems):
        rems.append(i % num)
        length += 1
        i = (i % num) * 10
    if length > maxlen:
        result = num
        maxlen = length

print result
