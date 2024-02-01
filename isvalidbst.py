class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        if root.left:
            if root.left.val>=root.val:
                return False
        if root.right:
            if root.right.val<=root.val:
                return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)
