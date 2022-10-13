from typing import List, Optional

from pylist import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        p = head
        res = 0
        nums = set(nums)

        while p is not None:
            while p is not None and p.val not in nums:
                p = p.next

            if p is not None:
                res += 1

            while p is not None and p.val in nums:
                p = p.next

        return res


head = [0, 1, 2, 3]
nums = [0, 1, 3]
# head = [0,1,2,3,4]
# nums = [0,3,1,4]
head = ListNode.fromList(head)
print(Solution().numComponents(head, nums))
