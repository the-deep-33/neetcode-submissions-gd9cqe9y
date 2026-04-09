class Solution:

    dictionary = {}
    dictionary[-1] = 0
    dictionary[0] = 0
    dictionary[1] = 1
    dictionary[2] = 2

    def climbStairs(self, n: int) -> int:
        if n in self.dictionary:
            return self.dictionary[n]

        result = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.dictionary[n] = result

        return result
        