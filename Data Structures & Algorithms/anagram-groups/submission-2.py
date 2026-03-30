class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = []
        svi = []
        for i in range(len(strs)):
            if i in seen:
                continue
                
            seen.append(i)
            lista = [strs[i]]
            
            for j in range(len(strs)):
                if j in seen:
                    continue
                if ''.join(sorted(strs[i])) == ''.join(sorted(strs[j])):
                    lista.append(strs[j])
                    seen.append(j)
            svi.append(lista)
        return svi
        