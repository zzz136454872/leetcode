from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int],
                    p4: List[int]) -> bool:
        p = [p1, p2, p3, p4]
        p.sort()
        p1, p2, p3, p4 = p

        print(p1, p2, p3, p4)

        if p1 == p2 or p2 == p3 or p3 == p4:
            return False

        def dot(a, b):
            return a[0] * b[0] + a[1] * b[1]

        def sub(a, b):
            return (a[0] - b[0], a[1] - b[1])

        def length2(a, b):
            return (a[0] - b[0])**2 + (a[1] - b[1])**2

        return dot(sub(p2, p1), sub(p3, p1)) == 0 and dot(
            sub(p2, p4), sub(p3, p4)) == 0 and dot(
                sub(p2, p1), sub(p2, p4)) == 0 and dot(sub(p3, p1), sub(
                    p3, p4)) == 0 and length2(p1, p2) == length2(p1, p3)


p1 = [0, 0]
p2 = [1, 1]
p3 = [1, 0]
p4 = [0, 1]

p1 = [0, 0]
p2 = [1, 1]
p3 = [1, 0]
p4 = [0, 12]

p1 = [1, 0]
p2 = [-1, 0]
p3 = [0, 1]
p4 = [0, -1]
print(Solution().validSquare(p1, p2, p3, p4))
