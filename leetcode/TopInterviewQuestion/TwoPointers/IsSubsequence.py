with open('../input.txt', 'r') as f:
    lines = f.readlines()
s = lines[0]
t = lines[1]
i = 0

for char in t:
    if char == s[i]:
        i+=1

print(i, len(s))
print(s)
if i!=len(s):
    print(False)
else:
    print(True)