class Solution:
    def searchMatrix(self, matrix, target):
        i = 0
        j = len(matrix) - 1

        while True:

            if matrix[i][0] <= target and matrix[i][len(matrix[0])-1] >= target:
                return self.binarySearchArray(matrix[i][:len(matrix[0])], target)

            elif matrix[j][0] <= target and matrix[j][len(matrix[0])-1] >= target:
                return self.binarySearchArray(matrix[j][:len(matrix[0])], target)

            if j <= i+1:
                return False

            else:
                diff = (j - i) // 2
                if matrix[i+diff][0] > target:
                    j = j - diff
                else:
                    i = i + diff

    def binarySearchArray(self, arr, target):
        if target in arr:
            return True
        return False
        """i = 0
        j = len(arr) - 1
        da = False

        while da:

            if arr[i] == target:
                return True
            if arr[j] == target:
                return j
            
            if arr[i+diff] == target:
                return i +
            diff = (j-i) // 2"""