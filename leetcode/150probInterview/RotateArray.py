class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        lst = nums.copy()
        for i in range(len(nums)):
            if i<k:
                nums[i]=lst[len(nums)-k+i]
            else:
                nums[i]=lst[i-k]