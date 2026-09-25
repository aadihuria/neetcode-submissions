class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        total2 = 1
        arr = []
        post = []
        for num in nums:
            total *= num
            arr.append(total)
        for i in range(len(nums) - 1, -1, -1):
            total2 *= nums[i]
            post.append(total2)
        post.reverse()
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(post[i + 1])
            elif i > 0 and i < (len(nums) - 1):
                res.append(arr[i - 1] * post[i + 1])
            else:
                res.append(arr[i - 1])
        return res