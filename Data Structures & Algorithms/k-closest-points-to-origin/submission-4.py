import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dictionary = {}

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]

            distance = math.sqrt(x ** 2 + y ** 2)

            p = (x, y)

            dictionary[p] = distance

        sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))

        lista = []

        result = list(sorted_dict.keys())[:k]

        return result

        