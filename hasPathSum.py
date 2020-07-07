from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        #print(sum)
        if root==None: 
            return False
        if root.left==None and root.right==None and sum==root.val:
            return True
        tmp=sum-root.val
        if root.left!=None and self.hasPathSum(root.left,tmp):
            return True
        if root.right!=None and self.hasPathSum(root.right,tmp):
            return True
        return False
        

sl=Solution()
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(8)

print(sl.hasPathSum(root,3))
