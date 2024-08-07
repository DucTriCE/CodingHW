with open('../input.txt', 'r') as f:
    lines = f.readlines()
s = lines[0]

# Using two pointers and not using built-in function
'''
s = s.lower()
tmp = ''

for i in s:
    if i>='a' and i<='z' or i>='0' and i<='9':
        tmp+=i
s = tmp

for i in range(len(s)):
    if s[i]!=s[len(s)-i-1]:
        print(False)
        exit()
print(True)
'''

s = s.lower()
s = ''.join(c for c in s if c.isalnum())
print(s==s[::-1])