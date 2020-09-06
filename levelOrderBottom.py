from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        queue1=[root]
        queue2=[]
        out=[]
        while len(queue1)!=0:
            tmp=[]
            while len(queue1)>0:
                tmp.append(queue1[0].val)
                if queue1[0].left!=None:
                    queue2.append(queue1[0].left)
                if queue1[0].right!=None:
                    queue2.append(queue1[0].right)
                del queue1[0]
            out.append(tmp)
            if len(queue2)==0:
                break
            tmp=[]
            while len(queue2)>0:
                tmp.append(queue2[0].val)
                if queue2[0].left!=None:
                    queue1.append(queue2[0].left)
                if queue2[0].right!=None:
                    queue1.append(queue2[0].right)
                del queue2[0]
            out.append(tmp)
        return out[::-1]
root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
sl=Solution()
print(sl.levelOrderBottom(root))
