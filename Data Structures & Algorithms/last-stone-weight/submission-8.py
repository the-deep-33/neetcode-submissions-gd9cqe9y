import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * (-1)
        heapq.heapify(stones)

        while len(stones) > 1:
            x = (-1) * heapq.heappop(stones)
            y = (-1) * heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, (-1) * abs(x - y))

        try:
            return -1*stones[0]
        except:
            return 0

        