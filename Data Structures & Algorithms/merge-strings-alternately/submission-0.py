class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        i = 0
        while i < len(word1) and i < len(word2):
            output += word1[i]
            output += word2[i]
            i += 1
        if i < len(word1):
            output += word1[i:]
            return output
        elif i < len(word2):
            output += word2[i:]
            return output
        else:
            return output

