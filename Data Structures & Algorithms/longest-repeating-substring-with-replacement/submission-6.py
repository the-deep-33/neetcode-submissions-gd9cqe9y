class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= k:
            return len(s)
        duzina = 1

        i = 0
        j = 1

        k1 = k

        while i < len(s) and j < len(s):
            if s[i] == s[j]:
                if j == len(s) - 1:
                    if k1 > 0:
                        duzina = max(duzina, min(len(s), j-i+1+k1))
                        i += 1
                        j = i + 1
                        break
                    else:
                        duzina = max(duzina, j-i+1)
                        i += 1
                        j = i + 1
                        break
                else:
                    j += 1
                continue
            if s[i] != s[j]:
                k1 -= 1
                if k1 == -1:
                    duzina = max(duzina, j-i)
                    k1 = k
                    if k == 0:
                        i = j
                        j = i+1
                    for r in range(i, j):
                        if s[i] != s[r]:
                            i = r
                            j = i+1
                            break
                else:
                    if j == len(s) - 1:
                        if k1 > 0:
                            duzina = max(duzina, min(len(s), j-i+1+k1))
                        else:
                            duzina = max(duzina, j-i+1)
                        i += 1
                        j = i + 1
                        k1 = k
                    else:
                        j += 1

        return duzina
            
            
            