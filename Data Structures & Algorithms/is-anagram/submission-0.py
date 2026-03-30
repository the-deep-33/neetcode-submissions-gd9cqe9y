class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = ''.join(sorted(s))
        string2 = ''.join(sorted(t))
        if len(string1) != len(string2):
            return False
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                return False
        return True
        