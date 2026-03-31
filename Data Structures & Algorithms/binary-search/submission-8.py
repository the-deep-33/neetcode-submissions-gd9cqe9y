class Solution:
    def search(self, nums, target):

        if target not in nums:
            return -1

        i = 0
        j = len(nums) - 1

        while True:
            
            if nums[i + (j-i) // 2] == target:
                return i + (j-i) // 2
            if nums[i + (j-i) // 2] > target:
                j = j - (j-i) // 2
            elif nums[i + (j-i) // 2] < target:
                i = i + (j-i) // 2

            if j == i+1:
                if nums[j] == target:
                    return j
                return i