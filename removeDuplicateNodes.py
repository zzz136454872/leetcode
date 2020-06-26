from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        log=set()
        tmp=head
        log.add(tmp.val)
    
        while tmp!=None and tmp.next!=None:
            if tmp.next.val in log:
                tmp2=tmp.next
                tmp.next=tmp2.next
            else:
                log.add(tmp.next.val)
                tmp=tmp.next
        return head
        
