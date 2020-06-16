
from typing import *

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        out=[]
        queue=[root]
        while len(queue)>0:
            node=queue.pop(0)
            if node!=None:
                out.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                out.append(None)
        return str(out)

    def deserialize(self, data):
        data=eval(data)
        if len(data)==1:
            return None
        root=TreeNode(data[0])
        queue=[root]
        data.pop(0)
        while len(data)>0:
            node=queue.pop(0)
            print(node)
            print(node.val)
            left=data.pop(0)
            right=data.pop(0)
            if left!=None:
                node.left=TreeNode(left)
                queue.append(node.left)
            if right!=None:
                node.right=TreeNode(right)
                queue.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.right.left=TreeNode(4)
root.right.right=TreeNode(5)
codec = Codec()
print(codec.serialize(root))
root=codec.deserialize(codec.serialize(root))
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.right.left.val)
print(root.right.right.val)
