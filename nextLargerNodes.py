from typing import List, Optional

from pylist import ListNode


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        p = head
        res = []
        stack = []
        i = 0

        while head != None:
            while len(stack) > 0 and stack[-1][0] < head.val:
                now = stack.pop()
                res[now[1]] = head.val
            stack.append((head.val, i))
            i += 1
            res.append(0)
            head = head.next

        return res


head = [2, 1, 5]
head = [2, 7, 4, 3, 5]
head = ListNode.fromList(head)
print(Solution().nextLargerNodes(head))
