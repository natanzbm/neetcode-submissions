# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        nodes = [root]

        for node in nodes:
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        for node in nodes:
            node.left, node.right = node.right, node.left

        return root