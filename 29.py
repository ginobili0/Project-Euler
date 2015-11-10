nums = []

for a in range(2, 101):
    for b in range(2, 101):
        c = a ** b
        if c not in nums: nums.append(c)

print len(nums)
