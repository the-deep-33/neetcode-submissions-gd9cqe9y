class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            number = target - nums[i]
            for j in range(len(nums)):
                if nums[j] == number and i != j:
                    return [i, j]
        