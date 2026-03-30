class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        string = str(n)
        brojac = 0
        for s in string:
            if s == "1":
                brojac += 1
        return brojac
        