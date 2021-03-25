from pylist import *
from typing import *

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_val=-12345
        new_head=ListNode(new_val)
        new_head.next=head
        p=new_head
        while p.next!=None:
            q=p.next
            r=q.next
            while r!=None and r.val==q.val:
                r=r.next
            if r!=q.next:
                p.next=r
            else:
                p=p.next
        return new_head.next

sl=Solution()
# 1->2->3->3->4->4->5
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(3)
head.next.next.next.next=ListNode(4)
head.next.next.next.next.next=ListNode(4)
head.next.next.next.next.next.next=ListNode(5)
ListNode.travel(head)
out=sl.deleteDuplicates(head)
ListNode.travel(out)
new_list=ListNode.fromList([])
ListNode.travel(new_list)
