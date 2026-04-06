class Solution:
    def findMin(self, nums):
        i = 0
        j = len(nums) - 1

        while i < j:
            mid = (i + j) // 2
            # Ako je nums[mid] veći od nums[j], znači da je
            # rotacija "presekla" niz negde desno od mid-a,
            # pa minimum mora biti u [mid+1, j]
            if nums[mid] > nums[j]:
                i = mid + 1
            # Inače, mid bi mogao biti minimum, ili je minimum levo,
            # pa zadržavamo mid u opsegu sa j = mid
            else:
                j = mid

        return nums[i]