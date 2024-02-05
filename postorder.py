# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        vals = []

        def post(node):
            if not node:
                return 
            post(node.left)
            post(node.right)
            vals.append(node.val)
        post(root)
        return vals 
        
