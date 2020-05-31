from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root,root)
    
    def check(self,a,b):
        if a==None and b==None:
            return True
        if a==None or b==None:
            return False
        if a.val!=b.val:
            return False
        return self.check(a.left,b.right) and self.check(a.right,b.left)

        

