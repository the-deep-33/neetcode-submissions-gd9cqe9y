class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums1 = nums.copy()
            del nums1[i]
            if nums[i] not in nums1:
                return nums[i]
        