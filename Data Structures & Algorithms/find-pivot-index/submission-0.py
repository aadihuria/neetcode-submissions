class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        prefix = []
        for num in nums:
            total += num
            prefix.append(total)
        for i in range(len(nums)):
            if self.prefixx(i, nums, prefix) == self.post(i, nums, prefix):
                return i
        return -1
    def prefixx(self, index: int, nums: List[int], prefix: List[int]):
        if index > 0:
            return prefix[index - 1]
        return 0
    def post(self, index: int, nums: List[int], prefix: List[int]):
        return prefix[-1] - prefix[index]