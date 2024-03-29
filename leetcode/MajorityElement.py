from collections import defaultdict 

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dct = defaultdict(int)
        for item in nums:
            dct[item]+=1
        for item, value in dct.items():
            if value > len(nums)//2:
                return item
