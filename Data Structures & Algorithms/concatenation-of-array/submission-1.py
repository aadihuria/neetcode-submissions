class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        l = 0
        while l < 2:
            for i in range(len(nums)):
                ans.append(nums[i])
            l += 1
        return ans