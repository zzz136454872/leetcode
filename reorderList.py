from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printlist(a):
    print(a.val)
    if a.next!=None:
        printlist(a.next)

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head==None:
            return
        p=head
        q=head
        while q!=None:
            pre_p=p
            p=p.next
            q=q.next
            if q!=None:
                q=q.next
        pre_p.next=None
        
        if p!=None:
            q=p.next
            p.next=None
            if q!=None:
                r=q.next
                while True:
                    q.next=p
                    p=q
                    q=r
                    if r!=None:
                        r=r.next
                    else:
                        break
            q=p
            p=head
        
            while q!=None:
                r=p.next
                p.next=q
                p=r
                r=q.next
                q.next=p
                q=r

inp=[ListNode(i+1) for i in range(2)]
for i in range(len(inp)-1):
    inp[i].next=inp[i+1]
sl=Solution()
sl.reorderList(inp[0])
p=inp[0]
while p!=None:
    print(p.val)
    p=p.next

                    
