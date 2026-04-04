class Solution:
    def checkInclusion(self, s1, s2):

        for i in range(len(s2)):
            
            if s2[i] in s1:
                s3 = sorted(s1)
                s4 = sorted(s2[i:i+len(s1)])
                da = True
                for j in range(len(s3)):
                    if j >= len(s4) or s3[j] != s4[j]:
                        da = False
                        break
                if da == True:
                    return True

        return False