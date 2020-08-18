from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        p=head
        log=[]
        while p!=None:
            log.append(p.val)
            p=p.next
        def buildTree(start,end):
            if start>end:
                return None
            mid=(start+end)//2
            root=TreeNode(val=log[mid])
            root.left=buildTree(start,mid-1)
            root.right=buildTree(mid+1,end)
        return buildTree(0,len(log)-1)


                

