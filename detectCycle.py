from pylist import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        p = head
        mem = set()

        while head != None:
            if head in mem:
                return head
            mem.add(head)
            head = head.next

        return None


head = [3, 2, 0, -4]
head = ListNode.fromList(head)
head.next.next.next.next = head.next

print(Solution().detectCycle(head))
