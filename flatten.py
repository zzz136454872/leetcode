from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root==None:
            return
        self.sub(root)

    def sub(self,root):
        if root.left!=None:
            self.sub(root.left)
        if root.right!=None:
            self.sub(root.right)
        if root.left!=None:
            tmp=root.right
            root.right=root.left
            root.left=None
            p=root
            while p.right!=None:
                p=p.right
            p.right=tmp
       
        
