from typing import List

from pylist import ListNode


# 不知道是哪个
class Solution1:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:
            head = ListNode(insertVal)
            head.next = head

            return head

        p = head.next
        q = head

        while p != head and p.val <= p.next.val:
            q = p
            p = p.next
        q = p
        p = p.next

        if p.val >= insertVal or q.val <= insertVal:
            q.next = ListNode(insertVal)
            q.next.next = p

            return head

        while p.val < insertVal:
            q = p
            p = p.next
        q.next = ListNode(insertVal)
        q.next.next = p

        return head


# head = [3, 4, 1]
# insertVal = 2
# head = []
# insertVal = 1
# head = [1]
# insertVal = 0
# head = ListNode.fromList(head)
#
# if head is not None:
#     head.getTail().next = head
# head = Solution().insert(head, insertVal)
# ListNode.travel(head)


class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])

        return res


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
intervals = [[1, 5]]
newInterval = [0, 3]
print(Solution().insert(intervals, newInterval))
