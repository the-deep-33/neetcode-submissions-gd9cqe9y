class Solution:
    def minEatingSpeed(self, piles, h):

        i = 1
        j = max(piles)

        while j >= i:

            mid = (i+j) // 2

            suma = 0
            for p in piles:
                suma += math.ceil(p / mid)
            
            if suma <= h:
                sol = mid
                j = mid
                if j == i:
                    i = j+1
                    break

            elif suma > h:
                i = mid + 1


        return sol