class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
            
        nums.sort()
        brojac = 1
        brojac1 = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i] == nums[i+1] - 1:
                brojac1 += 1
            else:
                if brojac1 > brojac:
                    brojac = brojac1
                
                brojac1 = 1

        if brojac1 > brojac:
            brojac = brojac1

        return brojac

        