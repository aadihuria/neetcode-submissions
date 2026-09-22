class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        l = 0
        if k <= 0:
            return False
        for r in range(len(nums)):
            if r - l > k:
                seen.remove(nums[l])
                l += 1
            if nums[r] in seen:
                return True
                
            seen.add(nums[r])
        return False
            
#k = 1
#seen = (1,0)
# nums = [1,0,1,1]
#         l
#             r