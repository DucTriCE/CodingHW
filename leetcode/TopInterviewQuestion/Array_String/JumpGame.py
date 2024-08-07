with open('../input.txt','r') as f:
    lines = f.readlines()
nums = list(map(int, lines[0].split(',')))

# Complicated way (not effective)
'''
i=0
while i<len(nums)-1:
    if nums[i]==0:
        print(False)
        exit()
    else:
        max_jump = nums[i]+i
        if max_jump >= len(nums)-1:
            print(True)
            exit()
        idx_jump = 0
        for j in range(i+1, max_jump+1):
            if nums[j]+j >= max_jump:
                max_jump = nums[j]+j
                idx_jump = j
        i=idx_jump
print(True)
'''

max_steps = 0
for i in nums:
    if max_steps < 0:
        print(False)
        exit()
    elif i>max_steps:
        max_steps=i
    max_steps-=1
print(True)
