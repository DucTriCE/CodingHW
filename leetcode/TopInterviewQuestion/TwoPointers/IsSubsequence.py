with open('../input.txt', 'r') as f:
    lines = f.readlines()
s = lines[0].strip()
t = lines[1].strip()

i = 0
for char in t:
    if i!=len(s) and char == s[i]:
        i+=1

if i!=len(s):
    print(False)
else:
    print(True)