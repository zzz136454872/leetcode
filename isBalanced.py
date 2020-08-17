from typing import *

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            if root==None:
                return 0
            l=check(root.left)
            r=check(root.right)
            if l<0 or r<0:
                return -1
            if abs(l-r)>1:
                return -1
            return max(l,r)
        if check(root)>=0:
            return True
        return False
        
