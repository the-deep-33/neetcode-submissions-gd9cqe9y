class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        smallest_left = 1001
        stack = []
        smaller_left = [0] * len(heights)
        smaller_right = [0] * len(heights)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                smaller_right[stack[-1]] = i - 1
                stack.pop()

            stack.append(i)

        while stack:
            smaller_right[stack[-1]] = len(heights) - 1
            stack.pop()
        
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                smaller_left[stack[-1]] = i + 1
                stack.pop()
            
            stack.append(i)

        while stack:
            smaller_left[stack[-1]] = 0
            stack.pop()

        print(smaller_left, end="\n\n")
        print(smaller_right, end="\n\n")

        suma = -1

        for i in range(len(heights)):
            suma1 = (smaller_right[i] - smaller_left[i] + 1) * heights[i]
            if suma1 > suma:
                suma = suma1

        return suma





        