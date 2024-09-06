with open('../input.txt', 'r') as f:
    lines = f.readlines()
s = lines[0]

left = right = 0
chars = set()
max_size = 0

while right<len(s):
    if s[right] not in chars:
        chars.add(s[right])
        max_size = max(max_size, right-left+1)
        right+=1
    else:
        while s[right] in chars:
            chars.remove(s[left])
            left+=1
print(max_size)

