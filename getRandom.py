from random import randint
from typing import Optional

from pylist import ListNode


# 不知道是哪个
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
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# sl = Solution(head)
#
# for i in range(10):
#     print(sl.getRandom())

# 链表随机节点

from random import randrange
from typing import Optional

from pylist import ListNode


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        p = self.head
        out = -1
        i = 0

        while p is not None:
            i += 1

            if randrange(i) == 0:
                out = p.val
            p = p.next

        return out


# Your Solution object will be instantiated and called as such:
head = [1, 2, 3]
head = ListNode.fromList(head)
obj = Solution(head)

for i in range(1000):
    print(obj.getRandom())
