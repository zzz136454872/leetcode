from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int],
                      colSum: List[int]) -> List[List[int]]:
        r = [[-rowSum[i], i] for i in range(len(rowSum))]
        c = [[-colSum[i], i] for i in range(len(colSum))]
        heapify(r)
        heapify(c)
        m = len(rowSum)
        n = len(colSum)
        res = [[0] * n for i in range(m)]

        while len(r) > 0 and len(c) > 0:
            rnow = heappop(r)
            cnow = heappop(c)

            if rnow[0] < cnow[0]:
                res[rnow[1]][cnow[1]] = -cnow[0]
                rnow[0] -= cnow[0]
                heappush(r, rnow)
            else:
                res[rnow[1]][cnow[1]] = -rnow[0]
                cnow[0] -= rnow[0]

                if cnow[0] != 0:
                    heappush(c, cnow)

        return res


rowSum = [3, 8]
colSum = [4, 7]
rowSum = [5, 7, 10]
colSum = [8, 6, 8]
rowSum = [14, 9]
colSum = [6, 9, 8]
rowSum = [1, 0]
colSum = [1]
print(Solution().restoreMatrix(rowSum, colSum))
