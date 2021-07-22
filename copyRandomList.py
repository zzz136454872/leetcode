import copy


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# 复制带随机指针的链表
class Solution1:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return copy.deepcopy(head)


# 上一个题的另一种解法
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        p = head
        q = Node(p.val)
        outHead = q
        mem = {p: q}

        while p is not None:
            p = p.next

            if p is None:
                break
            q.next = Node(p.val)
            q = q.next
            mem[p] = q
        mem[None] = None
        p = head
        q = outHead

        while p is not None:
            q.random = mem[p.random]
            p = p.next
            q = q.next

        return outHead
