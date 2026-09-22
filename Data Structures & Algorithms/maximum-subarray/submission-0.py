class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -float('inf')
        curSum = -float('inf')

        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum