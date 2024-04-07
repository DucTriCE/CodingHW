if __name__ == '__main__':
    nums = list(map(int, input().split()))
    for i in nums:
        if i==0:
            nums.remove(i)
            nums.append(i)
    print(nums)
