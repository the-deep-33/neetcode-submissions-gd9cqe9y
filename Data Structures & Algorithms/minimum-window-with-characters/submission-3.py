from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)

        string = ""
        length = len(s) + 1

        for i in range(len(s) - len(t) + 1):
            if s[i] in t:
                if len(t) == 1:
                    return s[i]
                window_count = {s[i]: 1}

                for j in range(i+1, len(s)):
                    window_count[s[j]] = window_count.get(s[j], 0) + 1

                    found = True

                    for char in t_counter:
                        if window_count.get(char, 0) < t_counter[char]:
                            found = False
                            break

                    if found == True:
                        length1 = j - i + 1
                        if length1 < length:
                            string = s[i:j+1]
                            length = length1

        return string

        