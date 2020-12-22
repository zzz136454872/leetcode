from typing import *
from pytree import TreeNode

class Solution:
    def zigzagLevelOrder(self,root):
        if root==None:
            return []
        stack1=[root]
        stack2=[]
        out=[]
        while len(stack1)>0:
            out.append([])
            while len(stack1)>0:
                node=stack1.pop()
                out[-1].append(node.val)
                if node.left!=None:
                    stack2.append(node.left)
                if node.right!=None:
                    stack2.append(node.right)
            if len(stack2)==0:
                break
            out.append([])
            while len(stack2)>0:
                node=stack2.pop()
                out[-1].append(node.val)
                if node.right!=None:
                    stack1.append(node.right)
                if node.left!=None:
                    stack1.append(node.left)
        return out

sl=Solution()
root=TreeNode(3)
root.left=TreeNode(9)
root.left.left=TreeNode(1)
root.left.right=TreeNode(3)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
print(sl.zigzagLevelOrder(root))
            
