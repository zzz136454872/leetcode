from typing import *
from pytree import *

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodeStack=[root] 
        self.flagStack=[0]

    def next(self) -> int:
        if len(self.nodeStack)==0:
            return -1
        while self.flagStack[-1]==0 and self.nodeStack[-1].left!=None:
            self.flagStack[-1]+=1
            self.nodeStack.append(self.nodeStack[-1].left)
            self.flagStack.append(0)
        nowNode=self.nodeStack.pop()
        self.flagStack.pop()
        if nowNode.right!=None:
            self.nodeStack.append(nowNode.right)
            self.flagStack.append(0)
        return nowNode.val

    def hasNext(self) -> bool:
        return len(self.nodeStack)>0

# inp=[7, 3, 15, null, null, 9, 20]
root=TreeNode(7)
root.left=TreeNode(3)
root.right=TreeNode(15)
root.right.left=TreeNode(9)
root.right.right=TreeNode(20)
# Your BSTIterator object will be instantiated and called as such:
obj = BSTIterator(root)
print(obj.next())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
