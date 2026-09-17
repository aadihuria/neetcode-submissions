class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m + n - 1
        o = m - 1
        t = n - 1
        while o >= 0 and t >= 0:
            if nums2[t] > nums1[o]:
                nums1[l] = nums2[t]
                t -= 1
            else:
                nums1[l] = nums1[o]
                o -= 1
            l -= 1
        while t >= 0:
            nums1[l] = nums2[t]
            t, l = t - 1, l - 1