class Solution:
    def search(self, nums: List[int], target: int) -> int:

        i = 0
        j = len(nums) - 1

        while i <= j:

            if i == j or i == j - 1:
                if nums[i] == target:
                    return i
                if nums[j] == target:
                    return j
                return -1
            
            mid = (i + j) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                if nums[j] > target:
                    if nums[j] < nums[mid]:
                        i = mid + 1
                    else:
                        j = mid
                elif nums[j] < target:
                    j = mid

                else:
                    return j
            
            else: 
                if nums[j] < target:
                    if nums[j] < nums[mid]:
                        i = mid+1
                    else:
                        j = mid
                else:
                    i = mid + 1
        