class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lista = set()
        for i in range(len(nums)):
            target = nums[i]*(-1)
            novi = nums.copy()
            novi = novi[i+1:]
            novi.sort()
            j = 0
            k = len(novi)-1
            while j < k:
                if novi[j] + novi[k] < target:
                    j += 1
                elif novi[j] + novi[k] > target:
                    k -= 1
                else:
                    l = [nums[i], novi[j], novi[k]]
                    l.sort()
                    lista.add(tuple(l))
                    k -= 1
                    j += 1
        return list(lista)
        