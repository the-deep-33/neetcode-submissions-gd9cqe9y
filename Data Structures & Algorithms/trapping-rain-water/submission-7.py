class Solution:

    def trap(self, height):

        dictionary1 = {}
        dictionary2 = {}

        i = 0
        j = len(height) - 1

        max_left = 0
        max_right = 0

        for i in range(len(height)):

            dictionary1[i] = max_left
            if height[i] > max_left:
                max_left = height[i]

        for j in range(len(height)-1, -1 , -1):

            dictionary2[j] = max_right
            if height[j] > max_right:
                max_right = height[j]

        suma = 0

        for i in range(len(height)):
            suma += max(min(dictionary1[i], dictionary2[i]) - height[i], 0)

        return suma