from typing import List

# TLE


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        head = Node(-1)
        p = head

        for num in nums:
            p.next = Node(num)
            p.next.prev = p
            p = p.next

        tail = Node(-1)
        p.next = tail
        tail.prev = p

        def gcd(a, b):
            while b > 0:
                a, b = b, a % b

            return a

        direction = 0

        while True:
            direction += 1
            notchange = True

            if direction % 2 == 1:
                p = head.next

                while p.next != tail:
                    g = gcd(p.val, p.next.val)

                    if g != 1:
                        p.val = p.val * p.next.val // g
                        p.next.next.prev = p
                        p.next = p.next.next
                        notchange = False
                    else:
                        p = p.next
            else:
                p = tail.prev

                while p.prev != head:
                    g = gcd(p.val, p.prev.val)

                    if g != 1:
                        p.val = p.val * p.prev.val // g
                        p.prev.prev.next = p
                        p.prev = p.prev.prev
                        notchange = False
                    else:
                        p = p.prev

            if notchange:
                break

        p = head.next
        out = []

        while p != None:
            out.append(p.val)
            p = p.next

        return out[:-1]


nums = [6, 4, 3, 2, 7, 6, 2]
nums = [2, 2, 1, 1, 3, 3, 3]
nums = [287, 41, 49, 287, 899, 23, 23, 20677, 5, 825]
nums = [2, 3, 2, 3, 2, 3, 6]
exp = [2009, 20677, 825]
print(Solution().replaceNonCoprimes(nums))
