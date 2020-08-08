from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:

        x=None
        y=None
        pre=None

        def midOrder(root_now,x,y,pre):
            if root_now==None:
                return x,y,pre
            x,y,pre=midOrder(root_now.left,x,y,pre)
            if pre!=None and pre.val>root_now.val:
                if x==None:
                    x=pre
                y=root_now
            pre=root_now
            x,y,pre=midOrder(root_now.right,x,y,pre)
            return x,y,pre
        x,y,pre=midOrder(root,x,y,pre)
        x.val,y.val=y.val,x.val

sl=Solution()
root=TreeNode(1)
root.left=TreeNode(3)
root.left.right=TreeNode(2)
sl.recoverTree(root)
print(root.val)
print(root.left.val)
print(root.left.right.val)
          
