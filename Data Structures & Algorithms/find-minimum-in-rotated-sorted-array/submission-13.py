class Solution:
    def findMin(self, nums):

        i = 0
        j = len(nums) - 1

        if i == j:
            return nums[i]

        if nums[0] > nums[1]:
            return nums[1]

        while i < j:
            print(f"i = {i}, j = {j}")
            mid = (i+j) // 2

            if nums[mid] > nums[j]:
                i = mid+1
            else:
                j = mid

        return nums[i]