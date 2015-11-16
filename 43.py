from itertools import permutations

perm = permutations('0123456789')

nums = []

for p in perm:
    nums.append(''.join(p))

total = 0

for num in nums:
    if int(num[1:4]) % 2 == 0 and int(num[2:5]) % 3 == 0 and int(num[3:6]) % 5 == 0 and int(num[4:7]) % 7 == 0 and int(num[5:8]) % 11 == 0 and int(num[6:9]) % 13 == 0 and int(num[7:10]) % 17 == 0:
        total += int(num)

print total