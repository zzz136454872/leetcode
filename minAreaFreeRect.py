from typing import List


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        def sub(a, b):
            return (a[0] - b[0], a[1] - b[1])

        def add(a, b):
            return (a[0] + b[0], a[1] + b[1])

        def mul(a, b):
            return a[0] * b[0] + a[1] * b[1]

        s = set()

        n = len(points)

        for i in range(n):
            points[i] = tuple(points[i])
            s.add(points[i])

        large = 1111222233334444555566667777

        res = large

        for i in range(n):
            for j in range(n):
                if j == i:
                    continue

                for k in range(n):
                    if k == i or k == j:
                        continue
                    v1 = sub(points[j], points[i])
                    v2 = sub(points[k], points[i])

                    if mul(v1, v2) == 0:
                        m = add(points[j], v2)

                        if m in s:
                            # print(i,points[i],j,points[j],k,points[k],v1,v2)
                            res = min(res, mul(v1, v1) * mul(v2, v2))

        if res == large:
            return 0

        return res**0.5


points = [[1, 2], [2, 1], [1, 0], [0, 1]]
points = [[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]]
print(Solution().minAreaFreeRect(points))
