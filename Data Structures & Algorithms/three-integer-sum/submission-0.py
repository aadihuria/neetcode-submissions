class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = sorted(nums)
        res = []
        total = 0
        for i, a in enumerate(n):
            if a > 0:
                break
            if i > 0 and a == n[i-1]:
                continue
        
            l,r = i + 1, len(n) - 1
            while l < r:
                total = (a + n[l] + n[r])
                if total == 0:
                    res.append([a, n[l], n[r]])
                    l += 1
                    r -= 1
                    while n[l] == n[l - 1] and l < r:
                        l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res


        # [-4,-1,-1,0,2,2]
        #.  a. l        r