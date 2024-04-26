if __name__ == '__main__':
    nums = list(map(int, input().split()))
    k = int(input())
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i]==nums[j] and abs(i-j)<=k:
    #             return True
    # return False
    dct = {}
    for idx, value in enumerate(nums):
        if value in dct and abs(idx-dct[value])<=k:
            print(True)
        dct[value]=idx
    print(False)