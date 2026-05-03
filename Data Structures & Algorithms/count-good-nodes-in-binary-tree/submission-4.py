# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def max_so_far(self, node, biggest = None):

        if node is None:
            return 0

        if biggest is None:
            biggest = node.val

        if node.val >= biggest:
            biggest = node.val
            return 1 + self.max_so_far(node.left, biggest) + self.max_so_far(node.right, biggest)

        return self.max_so_far(node.left, biggest) + self.max_so_far(node.right, biggest)

    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return self.max_so_far(root, None)

        
        