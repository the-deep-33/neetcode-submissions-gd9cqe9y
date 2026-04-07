class Solution:
    def isHappy(self, n: int) -> bool:
        n1 = n
        resenje = set()
        while True:
            suma = 0
            while n1 > 0:
                suma += pow(n1%10, 2)
                n1 = n1 // 10

            n1 = suma
            if suma == 1:
                return True
            if suma in resenje:
                return False
            resenje.add(suma)

        return True


            
        