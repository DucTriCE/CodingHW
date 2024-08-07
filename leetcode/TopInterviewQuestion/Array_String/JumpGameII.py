with open('../input.txt','r') as f:
    lines = f.readlines()
nums = list(map(int, lines[0].split(',')))

min_jump = 0
i=0
while i<len(nums)-1:
    max_jump = nums[i]+i
    if max_jump >= len(nums)-1:
        min_jump+=1
        print(min_jump)
        exit()
    idx_jump = 0
    for j in range(i+1, max_jump+1):
        if nums[j]+j >= max_jump:
            max_jump = nums[j]+j
            idx_jump = j
    i=idx_jump
    min_jump+=1
print(min_jump)
