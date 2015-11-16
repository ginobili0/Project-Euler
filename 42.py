f = open('p042_words.txt', 'r')

words = f.read().split(',')
words = [word.replace('\"', '') for word in words]

maxlen = max([len(word) for word in words])

## generate values for each letter
vals = {}
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for letter in letters:
    vals[letter] = letters.index(letter) + 1

## generate triangle numbers
trinums = []
for i in range(1, maxlen * 5):
    trinums.append(0.5 * i * (i + 1))

count = 0
for word in words:
    wordval = sum([vals[letter] for letter in word])
    if wordval in trinums: count += 1

print count


