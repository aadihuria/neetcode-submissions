class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        one = 0
        res = 0
        for num in nums:
            if num == 1:
                one += 1
            else:
                one = 0
            res = max(res, one)
        return res