# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return self.same(root.left,root.right)

    def same(self,q, r):
        if not q and not r:
            return True
        if not q or not r or q.val!=r.val:
            return False
        return self.same(q.left, r.right) and self.same(q.right, r.left)
        
