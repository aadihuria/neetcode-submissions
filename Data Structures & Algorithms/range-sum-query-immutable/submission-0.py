class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        right = self.prefix[right]
        if left > 0:
            left = self.prefix[left - 1]
        else:
            left = 0
        return right - left


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)