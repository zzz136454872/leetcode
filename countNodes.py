
from typing import *
from pytree import TreeNode

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root==None:
            return 0
        return 1+self.countNodes(root.left)+self.countNodes(root.right)

sl=Solution()
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
root=TreeNode(1)
root.left=TreeNode(2) 
root.left.left=TreeNode(4) 
root.left.right=TreeNode(5) 
root.right=TreeNode(3) 
root.right.left=TreeNode(6) 

print(sl.countNodes(root))
        
