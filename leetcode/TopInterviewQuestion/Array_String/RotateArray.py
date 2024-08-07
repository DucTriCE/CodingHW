with open('../input.txt','r') as f:
    lines = f.readlines()
nums = list(map(int, lines[0].split(',')))
k = int(lines[1])

# Easiest way
'''
k%=len(nums)
for i in range(k):
    nums.insert(0, nums[-1])
    nums.pop(-1)
print(nums)
'''

for i in range(k):
    nums.insert(0, nums.pop())