with open('../input.txt', 'r') as f:
    lines = f.readlines()
target = int(lines[0])
nums = list(map(int, lines[1].split(',')))

left = right = sum_subarray = 0
min_size = len(nums)+1

while right<len(nums):
    sum_subarray += nums[right]
    while sum_subarray >= target:
        sum_subarray -= nums[left]
        min_size = min(min_size, right-left+1)
        left+=1
    right+=1

print(min_size) if min_size!=len(nums)+1 else 0