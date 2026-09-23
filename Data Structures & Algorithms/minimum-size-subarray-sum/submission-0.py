class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        t = float('inf')
        curSum = 0
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                t = min(t, r - l + 1)
                curSum -= nums[l]
                l += 1
        if t == float('inf'):
            return 0
        return t
