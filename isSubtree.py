
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s==None:
            return False
        if self.same(s,t):
            return True
        if self.isSubTree(s.left) or self.isSubTree(s.right):
            return True
        return False


    def same(self, s: TreeNode, t: TreeNode) -> bool:
        if s==None:
            if t==None:
                return True
            return False
        if t==None:
            return False
        if s.val!=t.val:
            return False
        if not self.same(s.left,t.left) or not self.same(s.right,t.right):
            return False
        return True
