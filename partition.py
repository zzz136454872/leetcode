from typing import *
from pylist import ListNode

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        head1=None
        head2=None
        tail1=None
        tail2=None
        while head!=None:
            tmp=head
            head=head.next
            tmp.next=None
            if tmp.val<x:
                if tail1==None:
                    tail1=tmp
                    head1=tmp
                else:
                    tail1.next=tmp
                    tail1=tmp
            else:
                if tail2==None:
                    tail2=tmp
                    head2=tmp
                else:
                    tail2.next=tmp
                    tail2=tmp
        if head1==None:
            return head2
        tail1.next=head2
        return head1

sl=Solution()
inp=ListNode(1)
inp.next=ListNode(4)
inp.next.next=ListNode(3)
inp.next.next.next=ListNode(2)
inp.next.next.next.next=ListNode(5)
inp.next.next.next.next.next=ListNode(2)

x=3
out=sl.partition(inp,x)

ListNode.travel(out)
