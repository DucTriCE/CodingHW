class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        tmp = 1

        for j in range(1, len(nums)):
            if nums[j]==nums[i]:
                tmp+=1
                if tmp<3:
                    nums[i+1]=nums[j]
                    i+=1
                else:     
                    continue
            else:
                tmp=1
                nums[i+1]=nums[j]
                i+=1
        return i+1
                