from typing import *

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head=root
        while head!=None:
            nextHead=None
            pre=None
            while head!=None:
                if head.left!=None:
                    if nextHead==None:
                        nextHead=head.left
                    if pre!=None:
                        pre.next=head.left
                    pre=head.left
                if head.right!=None:
                    if nextHead==None:
                        nextHead=head.right
                    if pre!=None:
                        pre.next=head.right
                    pre=head.right
                head=head.next
            head=nextHead
        return root

sl=Solution()
root=Node(1)
root.left=Node(2)
root.left.left=Node(4)
root.left.right=Node(5)
root.right=Node(3)
root=sl.connect(root)
print(root.left.left.next.val)

