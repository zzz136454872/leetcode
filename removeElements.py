from pylist import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        nhead = None
        p = head
        tail = None

        while p is not None:
            if p.val != val:
                if nhead is None:
                    nhead = p
                else:
                    tail.next = p
                tail = p
            p = p.next
        if tail is not None:
            tail.next = None

        return nhead


sl = Solution()
head = [6, 1, 2, 6, 3, 4, 5, 6]
val = 6
head = ListNode.fromList(head)
out = sl.removeElements(head, val)
ListNode.travel(out)
