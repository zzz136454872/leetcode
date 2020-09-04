from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root==None:
            return []
        stack=[]
        out=[]
        def print_path(root):
            if root.left==None and root.right==None:
                tmp=''
                for i in stack:
                    tmp+=i+'->'
                out.append(tmp+str(root.val))
            else:
                stack.append(str(root.val))
                if root.left!=None:
                    print_path(root.left)
                if root.right!=None:
                    print_path(root.right)
                stack.pop()
        print_path(root)
        return out

sl=Solution()
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(5)
print(sl.binaryTreePaths(root))
                
               
            
