from collections import defaultdict
with open('../input.txt', 'r') as f:
    lines = f.readlines()

nums = list(map(int, lines[0].split()))

dict = defaultdict(int)

idx = 0
for i in range(len(nums)):
    dict[nums[i]]+=1
    if dict[nums[i]]<=2:
        nums[idx]=nums[i]
        idx+=1

print(nums[:idx])