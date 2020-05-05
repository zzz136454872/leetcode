

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:
        self.now=-1000000000000000
        return self.goThrough(root)
    
    def goThrough(self, root):
        if root==None:
            return True
        if not self.goThrough(root.left):
            return False
        if root.val<=self.now:
            return False
        self.now=root.val
        return self.goThrough(root.right)


