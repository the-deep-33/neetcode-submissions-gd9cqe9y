import math

class Solution:
    def dailyTemperatures(self, temperatures):

        stack = []
        result = []

        result.insert(0, 0)
        stack.append((temperatures[len(temperatures) - 1], len(temperatures) - 1))
        

        for i in range(len(temperatures) - 2, -1, -1):
            da = False

            while len(stack) > 0 and temperatures[i] >= stack[-1][0]:
                da = True
                stack.pop()

            if da == True and len(stack) == 0:
                result.insert(0, 0)
            elif da == True and len(stack) > 0:
                result.insert(0, stack[-1][1] - i)
            elif da == False:
                result.insert(0, 1)

                

            stack.append((temperatures[i], i))

        return result