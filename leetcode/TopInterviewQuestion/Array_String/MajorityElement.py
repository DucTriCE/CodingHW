with open('../input.txt','r') as f:
    lines = f.readlines()
nums = list(map(int, lines[0].split(',')))

# Easiest way
'''
nums.sort()
print(nums[len(nums)//2])
'''

from collections import Counter
count = Counter(nums)
print(max(count, key=count.get))