from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        lista = []

        for i, num in enumerate(nums):
            if k == 1:
                lista.append(num)
                continue

            
            while deq:
                if deq[0] < i - k + 1:
                    deq.popleft()
                elif nums[deq[-1]] < num:
                    deq.pop()
                else:
                    break

            deq.append(i)

            if i >= k-1:    
                lista.append(nums[deq[0]])
        
        return lista

        
        