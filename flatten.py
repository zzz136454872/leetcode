from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 不知道是什么
class Solution1:
    def flatten(self, root: TreeNode) -> None:
        if root == None:
            return
        self.sub(root)

    def sub(self, root):
        if root.left != None:
            self.sub(root.left)

        if root.right != None:
            self.sub(root.right)

        if root.left != None:
            tmp = root.right
            root.right = root.left
            root.left = None
            p = root

            while p.right != None:
                p = p.right
            p.right = tmp


# 扁平化多级双向链表


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def flattenSub(head):
            if head is None:
                return (None, None)
            p = head
            prev = p

            while p is not None:
                if p.child is not None:
                    q = p.next
                    tmp = flattenSub(p.child)
                    p.child = None
                    p.next = tmp[0]
                    tmp[0].prev = p
                    tmp[1].next = q

                    if q is not None:
                        q.prev = tmp[1]
                    prev = tmp[1]
                    p = q
                else:
                    prev = p
                    p = p.next

            return (head, prev)

        return flattenSub(head)[0]
