class Solution:
    def countBits(self, n: int) -> List[int]:
        lista = []

        for i in range(n+1):
            brojac = 0
            string = str(bin(i))
            for s in string:
                if s == '1':
                    brojac += 1
            lista.append(brojac)

        return lista