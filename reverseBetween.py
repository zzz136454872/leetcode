from typing import *
from pylist import *

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        p=ListNode(-1)
        new_head=p
        p.next=head
        for i in range(left-1):
            p=p.next
        q=p.next
        pre=p
        r=q.next
        for i in range(right-left):
            p=q
            q=r
            r=r.next
            q.next=p
        pre.next.next=r
        pre.next=q
        return new_head.next

sl=Solution()
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
left=1
right=5
nhead=sl.reverseBetween(head,left,right)
ListNode.travel(nhead)
        
