# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        deq = deque()
        result = []

        deq.append(root)

        while deq:
            lista = []
            for i in range(len(deq)):
                node = deq.popleft()
                lista.append(node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)

            result.append(lista)

        return result
        
        