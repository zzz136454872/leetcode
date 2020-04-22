from typing import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        root.level=1
        buf=[root]
        out=[root.val]
        now=1
        while len(buf)>0:
            head=buf[0]
            del buf[0]
            if head.level > now:
                now=head.level
                out.append(head.val)
            else:
                out[-1]=head.val
            if head.left!=None:
                head.left.level=now+1
                buf.append(head.left)
            if head.right!=None:
                head.right.level=now+1
                buf.append(head.right)
        return out

