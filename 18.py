f = open('prob-18.txt')
nums = []
for line in f:
    n = [int(i) for i in line.rstrip('\n').split(' ')]
    nums.append(n)

res = nums.pop()
while nums:
    temp = nums.pop()
    res = [(temp[i] + max(res[i], res[i + 1])) for i in xrange(len(temp))]
print res