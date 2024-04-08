if __name__ == '__main__':
    # Add your code here
    nums = list(map(int, input().split()))
    target = int(input())
    for i in range(len(nums)):
        if nums[i]<target:
            continue
        else:
            print(i)
    print(i+1)