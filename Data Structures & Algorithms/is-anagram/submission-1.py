class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = {}
        t1 = {}
        for cs, ct in zip(s, t):
            s1[cs] = s1.get(cs, 0) + 1
            t1[ct] = t1.get(ct, 0) + 1
        return s1 == t1
        