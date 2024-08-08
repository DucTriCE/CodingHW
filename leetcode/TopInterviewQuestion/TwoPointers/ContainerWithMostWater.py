with open('../input.txt', 'r') as f:
    lines = f.readlines()
height = list(map(int, lines[0].split(',')))

n = len(height)
left, right = 0, n-1
water = 0

while left < right:
    water = max(water, (right-left)*min(height[left], height[right]))
    if height[left] < height[right]:
        left+=1
    else:
        right-=1

print(water)