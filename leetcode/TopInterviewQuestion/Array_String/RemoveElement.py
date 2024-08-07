with open('../input.txt', 'r') as f:
    lines = f.readlines()

nums = list(map(int, lines[0].split()))
val = int(lines[1])

# Easiest way
'''
while val in nums:
    nums.remove(val)
'''

idx = 0
for i in range(len(nums)):
    if nums[i]!=val:
        nums[idx]=nums[i]
        idx+=1
print(nums[:idx])