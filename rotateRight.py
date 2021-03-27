from typing import *
from pylist import *

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head==None or head.next==None:
            return head
        length=0
        p=head
        tail=p
        while p!=None:
            tail=p
            p=p.next
            length+=1
        k=k%length
        if not k:
            return head
        rest=length-k-1
        p=head
        while rest>0:
            rest-=1
            p=p.next
        q=p.next
        p.next=None
        tail.next=head
        return q

nums=[0,1,2]
k=4
head=ListNode.fromList(nums)
sl=Solution()
out=sl.rotateRight(head,k)
ListNode.travel(out)
        
