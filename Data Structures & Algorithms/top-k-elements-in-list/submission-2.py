class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])
        # bucket =[], [], [], [], [], [], []
        #.         0.  1.  2   3   4.  5  6
        for val, freq in freq.items():
            bucket[freq].append(val)
        # bucket =[], [1], [2], [3], [], [], []
        #.         0.  1.  2   3   4.  5  6
        t = 0
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            if not bucket[i]:
                continue
            for val in bucket[i]:
                res.append(val)
                t += 1
                if t == k:
                    return res