class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
