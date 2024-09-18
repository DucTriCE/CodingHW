with open('../input.txt', 'r') as f:
    lines = f.readlines()
s = lines[0]

#Easiest way O(n^2)
'''
if not s:
    print(0)
    exit()

max_len = 1
for i in range(len(s)-1):
    st = set(s[i])
    for j in range(i+1, len(s)):
        if s[j] in st:
            max_len = max(max_len, len(st))
            break
        else:
            st.add(s[j])
            current_len = len(st)
print(max_len)
'''

#Smart way
chars = set()
left = right = 0
max_len = 0
while right < len(s):
    if s[right] not in chars:
        chars.add(s[right])
        max_len = max(max_len, right-left+1)
        right+=1
    else:
        while s[right] in chars:
            chars.remove(s[left])
            left+=1
print(max_len)
