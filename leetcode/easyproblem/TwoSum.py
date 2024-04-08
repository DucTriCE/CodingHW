if __name__ == '__main__':
    # Add your code here
    nums = list(map(int, input().split()))
    target = int(input())
    tmp = nums.copy()
    nums.sort()
    i, j = 0, len(nums)-1
    while i<j:
        if nums[i]+nums[j]>target:
            j-=1
        elif nums[i]+nums[j]<target:
            i+=1
        else:
            print(tmp.index(nums[i]), len(tmp)-tmp[::-1].index(nums[j])-1)
            break