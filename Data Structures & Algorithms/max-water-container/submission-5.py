class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        imaVeciLevo = dict()
        imaVeciDesno = dict()

        maxLevo = -1

        for i in range(len(heights)):
            if heights[i] >= maxLevo:
                imaVeciLevo[i] = False
                maxLevo = heights[i]
            else:
                imaVeciLevo[i] = True

        maxDesno = -1

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] >= maxDesno:
                imaVeciDesno[i] = False
                maxDesno = heights[i]
            else:
                imaVeciDesno[i] = True


        suma = min(heights[i], heights[j]) * (j - i)

        while i < j:
            print(f"i = {i}, j = {j}")
            if imaVeciDesno[i] == False and imaVeciLevo[j] == False:
                if suma < min(heights[i], heights[j]) * (j - i):
                    suma = min(heights[i], heights[j]) * (j - i)
                break
            
            if suma < min(heights[i], heights[j]) * (j - i):
                suma = min(heights[i], heights[j]) * (j - i)
            if heights[i] > heights[j]:
                j -= 1
            elif heights[i] < heights[j]:
                i += 1
            else:
                i += 1
                j -= 1

        return suma
