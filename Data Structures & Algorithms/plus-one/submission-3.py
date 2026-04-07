class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if digits[len(digits) - 1] != 9:
            digits[len(digits) - 1] = digits[len(digits) - 1] + 1

        else:
            i = len(digits) - 1
            while digits[i] == 9:
                digits[i] = 0
                i -= 1

            if i == -1:
                digits.insert(0, 1)
            else:
                digits[i] = digits[i] + 1

        return digits
        