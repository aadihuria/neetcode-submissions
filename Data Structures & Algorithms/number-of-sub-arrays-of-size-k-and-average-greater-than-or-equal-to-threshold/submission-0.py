class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l = 0
        avg = 0
        curSum = 0
        for r in range(len(arr)):
            curSum += arr[r]
            if r - l + 1 > k:
                curSum -= arr[l]
                l += 1
            avg = curSum / k
            if r - l + 1 == k:
                if avg >= threshold:
                    res += 1
        return res
