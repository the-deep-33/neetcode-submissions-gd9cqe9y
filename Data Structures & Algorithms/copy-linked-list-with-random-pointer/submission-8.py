"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        current = head

        dictionary = dict()

        while current:
            node = Node(current.val, None, None)
            temp = head
            dictionary[current] = node
            current = current.next

        current = head

        while current:
            dictionary[current].next = dictionary.get(current.next, None)
            dictionary[current].random = dictionary.get(current.random, None)
            current = current.next

        return dictionary.get(head, None)

        