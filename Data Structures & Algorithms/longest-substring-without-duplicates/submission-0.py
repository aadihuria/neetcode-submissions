class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep a set with characters, and a window and two pointers. move r forward and keep track of window size, if character is already in the set, then remove character from set and increment l and k eep going
        seen = set()
        l = 0
        t = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            t = max(t, r - l + 1)
        return t