class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        brojevi = set()

        for n in nums:
            if n in brojevi:
                return n
            brojevi.add(n)
        