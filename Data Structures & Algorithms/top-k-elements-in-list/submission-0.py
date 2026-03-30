class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vidjeni = {}
        for i, number in enumerate(nums):
            if number not in vidjeni.keys():
                vidjeni[number] = 1
            else:
                vidjeni[number] += 1
        sorted_vidjeni = sorted(vidjeni, key=lambda x: vidjeni[x], reverse=True)
        return sorted_vidjeni[:k]
        
        