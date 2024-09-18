with open('../input.txt', 'r') as f:
    lines = f.readlines()
s = lines[0]
words = lines[1].split(',')

#Out of memory way

def find_permutations(permutations, words, idx):
    if idx == len(words):
        word = ''.join(words[:])
        if word not in permutations:
            permutations.append(word)
            return
        else:
            return

    for i in range(idx, len(words)):
        words[i], words[idx] = words[idx], words[i]
        find_permutations(permutations, words, idx + 1)
        words[i], words[idx] = words[idx], words[i]


permutations = []
result = []
length = len(words[0])*len(words)

find_permutations(permutations, words, 0)
# print(permutations)
for i in range(0, len(s)):
    if i + length < len(s):
        word = ''.join(s[i:i+length])
        print(word)
        if word in permutations:
            result.append(i)
print(result)


#Smart way