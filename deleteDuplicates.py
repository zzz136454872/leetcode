from typing import *

from pylist import *


# 删除排序链表中的重复元素II
class Solution1:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_val = -12345
        new_head = ListNode(new_val)
        new_head.next = head
        p = new_head

        while p.next != None:
            q = p.next
            r = q.next

            while r != None and r.val == q.val:
                r = r.next

            if r != q.next:
                p.next = r
            else:
                p = p.next

        return new_head.next


# 删除排序链表中的重复元素
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_val = -12345
        new_head = ListNode(new_val)
        new_head.next = head
        p = new_head

        while p != None:
            q = p.next

            while q != None and q.val == p.val:
                q = q.next
            p.next = q
            p = q

        return new_head.next


sl = Solution()
# 1->2->3->3->4->4->5
inp = [1, 1, 2, 3, 3]
head = ListNode.fromList(inp)
ListNode.travel(head)
out = sl.deleteDuplicates(head)
ListNode.travel(out)
