class Solution:
    def getSum(self, a: int, b: int) -> int:
        negativa = 1
        negativb = 1
        if a < 0:
            a = bin(a)[3:]
            negativa = -1

        else:
            a = bin(a)[2:]

        if b < 0:
            b = bin(b)[3:]
            negativb = -1
        else:
            b = bin(b)[2:]

        a = list(reversed(a))
        b = list(reversed(b))

        suma = 0

        for i in range(min(len(a), len(b))):
            suma += negativa * int(a[i]) * pow(2, i) + negativb * int(b[i]) * pow(2, i)

        i += 1

        for j in range(i, len(a)):
            try:
                suma += negativa * int(a[j]) * pow(2, j)
            except:
                break

        for j in range(i, len(b)):
            try:
                suma += negativb * int(b[j]) * pow(2, j)
            except:
                break

        return suma


        

        