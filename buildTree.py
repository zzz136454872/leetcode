from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def printTree(root):
    if root!=None:
        print(root.val)
        printTree(root.left)
        printTree(root.right)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if(len(preorder)==0):
            return None
        root=TreeNode(preorder[0])
        mid=inorder.index(root.val)
        root.left=self.buildTree(preorder[1:mid+1],inorder[0:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
sl=Solution()
printTree(sl.buildTree(preorder,inorder))

