class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        negativ = False
        if x[0] == '-':
            negativ = True
            y = ''.join(list(reversed(x[1:])))
            return int("-" + y) if int("-" + y) > pow(2,31) * (-1) else 0
        else:
            y = ''.join(list(reversed(x)))
            print(y)
            return int(y) if int(y) < pow(2,31) - 1 else 0