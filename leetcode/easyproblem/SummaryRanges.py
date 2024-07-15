def summaryRanges(nums):
    lst = []
    left = right = 0
    if len(nums)==1:
        lst.append(str(nums[0]))
        return lst
    for i in range (1, len(nums)):
        if nums[i]!=nums[i-1]+1:
            right = i-1
            ranges = str(nums[left]) + '->' + str(nums[right]) if left!=right else str(nums[left])
            lst.append(ranges)
            left = i
            if i == len(nums)-1:
                lst.append(str(nums[i]))
        else:
            if i != len(nums)-1:
                continue
            else:
                right = i
                ranges = str(nums[left]) + '->' + str(nums[right]) if left!=right else str(nums[left])
                lst.append(ranges)
    return lst

if __name__ == '__main__':
    # nums = list(map(int, input().split()))
    nums = [0]
    sorted_unique = summaryRanges(nums)
    print(sorted_unique)