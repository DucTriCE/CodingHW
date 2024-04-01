def Solve(target, nums):
    count=0
    value=0
    print(nums)
    for i in nums:
        value+=i
        print(i, value)
        count+=1
        if value>=target:
            return count
    return 0


if __name__ == '__main__':
    target = 213
    nums = [12,28,83,4,25,26,25,2,25,25,25,12]
    print(Solve(target, nums))