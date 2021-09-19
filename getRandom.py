from random import randint
from typing import Optional

from pylist import ListNode


class Solution:
    def __init__(self, head: Optional[ListNode]):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, 
        so it contains at least one node.
        """
        self.list = []

        while head is not None:
            self.list.append(head.val)
            head = head.next
        self.n = len(self.list)

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """

        return self.list[randint(0, self.n - 1)]


# Your Solution object will be instantiated and called as such:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
sl = Solution(head)

for i in range(10):
    print(sl.getRandom())
