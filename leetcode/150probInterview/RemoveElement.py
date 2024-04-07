class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k=len(nums)-nums.count(val)
        while val in nums:
            nums.remove(val)
        return k