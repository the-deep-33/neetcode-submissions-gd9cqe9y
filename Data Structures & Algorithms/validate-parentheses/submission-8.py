class Solution:
    def isValid(self, s: str) -> bool:
        lista = []

        i = 0

        while i < len(s):

            if s[i] in "({[":
                lista.append(s[i])

            else:
                if s[i] == "]" and (len(lista) == 0 or lista[-1] != "["):
                    return False

                elif s[i] == "}" and (len(lista) == 0 or lista[-1] != "{"):
                    return False

                elif s[i] == ")" and (len(lista) == 0 or lista[-1] != "("):
                    return False

                else:
                    lista.pop()

            i += 1

        if len(lista) > 0:
            return False

        return True
                
            
            
            


        