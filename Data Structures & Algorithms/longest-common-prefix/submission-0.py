class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        for c in strs[0]:
            for word in strs[1:]:
                if i >= len(word):
                    return strs[0][:i]
                if word[i] != c:
                    return strs[0][:i]
                    
            i += 1
        return strs[0][:i]