class Solution:
    def reverseBits(self, n: int) -> int:

        string = str(bin(n))
        string = string[2:]
        string = string[::-1]
        while len(string) < 32:
            string += "0"
        
        n = int(string, 2)

        return n
        