from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int,
                       k: int) -> int:
        m = 0

        while m < len(fruits) and fruits[m][0] < startPos:
            m += 1
        l = m - 1
        r = m
        tmp = 0
        res = 0

        while l >= 0 and startPos - fruits[l][0] <= k:
            tmp += fruits[l][1]
            l -= 1

        for i in range(l + 1, min(m + 1, len(fruits))):
            while r < len(fruits) and 2 * (fruits[r][0] - startPos) + max(
                    0, startPos - fruits[i][0]) <= k:
                tmp += fruits[r][1]
                r += 1
            res = max(res, tmp)
            tmp -= fruits[i][1]

        l = m - 1
        r = m
        tmp = 0
        # print('m',m)

        while l >= 0 and 2 * (startPos - fruits[l][0]) <= k:
            tmp += fruits[l][1]
            l -= 1

        for i in range(l + 1, min(m + 1, len(fruits))):
            while r < len(fruits) and fruits[r][0] - startPos + 2 * max(
                    0, startPos - fruits[i][0]) <= k:
                tmp += fruits[r][1]
                r += 1
            # print(i,r,fruits[i],fruits[r-1],tmp)
            res = max(res, tmp)
            tmp -= fruits[i][1]

        return res


fruits = [[2, 8], [6, 3], [8, 6]]
startPos = 5
k = 4
fruits = [[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]]
startPos = 5
k = 4
fruits = [[0, 3], [3, 4], [8, 5]]
startPos = 3
k = 0
fruits = [[0, 10000]]
startPos = 200000
k = 200000

fruits = [[0, 7], [7, 4], [9, 10], [12, 6], [14, 8], [16, 5], [17, 8], [19, 4],
          [20, 1], [21, 3], [24, 3], [25, 3], [26, 1], [28, 10], [30, 9],
          [31, 6], [32, 1], [37, 5], [40, 9]]
startPos = 21
k = 30
print(sum(f[1] for f in fruits))
print(Solution().maxTotalFruits(fruits, startPos, k))
