with open('../input.txt','r') as f:
    lines = f.readlines()

strs = [word.strip().strip('"') for word in lines[0].split(',')]

if len(strs)==1:
    print(strs[0])
    exit()

min_length = len(min(strs, key=len))
longest_common_prefix = ''

for i in range(min_length):
    s = strs[0][i]
    for j in range(1, len(strs)):
        if s==strs[j][i] and j==len(strs)-1:
            longest_common_prefix += s
        elif s!=strs[j][i]:
            print(longest_common_prefix)
            exit()

print(longest_common_prefix)
