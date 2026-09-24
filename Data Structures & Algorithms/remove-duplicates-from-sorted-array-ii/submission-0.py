class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        freq = {}
        for r in range(len(nums)):
            if freq.get(nums[r], 0) >= 2:
                continue
            else:
                nums[l] = nums[r]
                l += 1
            freq[nums[r]] = freq.get(nums[r], 0) + 1
        return l
