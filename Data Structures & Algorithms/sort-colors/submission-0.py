class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for r in range(1, len(nums)):
            l = r - 1
            while l >= 0 and nums[r-1] > nums[r]:
                temp = nums[r-1]
                nums[r-1] = nums[r]
                nums[r] = temp
                l -= 1
                r -= 1
        