with open('../input.txt','r') as f:
    lines = f.readlines()
haystack = lines[0]
needle = lines[1]

n = len(needle)
# Original way
'''
for i in range(len(haystack)):
    # Out of range doesn't affect in slicing
    if needle==haystack[i:i+n]:
        print(i)
        exit()
'''

idx = haystack.find(needle)
print(idx)