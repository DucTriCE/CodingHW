with open('../input.txt','r') as f:
    lines = f.readlines()
height = list(map(int, lines[0].split(',')))

# Naive way (didnt work)
'''
water = 0
left = 0
if height[0]==0:
    height.pop(0)
for i in range(1, len(height)):
    if height[i]>=height[left]:
        water+=min(height[i], height[left])*(i-left-1) - sum(height[left+1:i])
        left=i
        print(water)
print(water)
'''

n = len(height)
left, right = 0, n-1
max_left = max_right = 0
water = 0

while left<right:
    if height[left] <= height[right]:
        if height[left]>=max_left:
            max_left = height[left]
        else:
            water += max_left - height[left]
        left+=1
    else:
        if height[right]>=max_right:
            max_right = height[right]
        else:
            water += max_right - height[right]
        right-=1

print(water)
