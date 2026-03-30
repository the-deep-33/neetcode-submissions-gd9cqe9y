class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lista = {}
        for i, string in enumerate(strs):
            sortirani = ''.join(sorted(string))
            if sortirani not in lista.keys():
                lista[sortirani] = []
            lista[sortirani].append(string)
        return list(lista.values())

        