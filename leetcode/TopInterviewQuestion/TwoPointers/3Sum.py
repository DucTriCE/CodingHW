with open('../input.txt', 'r') as f:
    lines = f.readlines()
nums = list(map(int, lines[0].split(',')))

n = len(nums)
nums.sort()
ans = set()
for i in range(n-2):
    first_num = nums[i]
    if first_num>0:
        break
    left, right = i+1, n-1
    if i==0 or nums[i]!=nums[i-1]:
        while left < right:
            if nums[left] + nums[right] + first_num == 0:
                second_num = nums[left]
                third_num = nums[right]
                ans.add((first_num, second_num, third_num))
                left+=1
                right-=1
            elif nums[left] + nums[right] + first_num > 0:
                right-=1
            else:
                left+=1

print(list(ans))