class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duzina = 1
        i = 0
        j = 1
        while i < len(s) and j < len(s):
            if i == j:
                j += 1
                continue
            if s[j] in s[i:j] or s[i] == s[j]:
                duzina = max(duzina, j-i)
                i += 1
                continue
            if j == len(s) - 1:
                duzina = max(duzina, j-i+1)
            j += 1
        if len(s) == 0:
            duzina = 0
        return duzina
            
        