class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        lista = []
        for i in range(len(nums)):
            product *= nums[i]

        for i in range(len(nums)):
            try:
                lista.append(product // nums[i])
            except ZeroDivisionError:
                product1 = 1
                nova = [num for j, num in enumerate(nums) if i != j]
                for num in nova:
                    product1 *= num
                lista.append(product1)

        return lista

        