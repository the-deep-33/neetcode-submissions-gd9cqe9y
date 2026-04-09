import collections
import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        broj = len(position)
        if broj == 1:
            return 1

        dictionary = {}
        for i in range(len(position)):
            dictionary[position[i]] = speed[i]

        dictionary = collections.OrderedDict(sorted(dictionary.items()))

        moment = (target - list(dictionary)[len(dictionary) - 1]) / list(dictionary.values())[len(dictionary) - 1]

        print(moment)

        for i in range(len(dictionary) - 2, -1, -1):
            moment1 = (target - list(dictionary)[i]) / list(dictionary.values())[i]
            print(moment1)
            if moment1 <= moment:
                broj -= 1
            else:
                moment = moment1

        return broj




        
        