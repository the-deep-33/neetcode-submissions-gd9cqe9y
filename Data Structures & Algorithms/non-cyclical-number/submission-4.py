class Solution:
    def isHappy(self, n: int) -> bool:
        n1 = n
        for i in range(100):
            suma = 0
            while n1 > 0:
                suma += pow(n1%10, 2)
                n1 = n1 // 10

            n1 = suma
            print(n1)

        if n1 == 1:
            return True

        return False


            
        