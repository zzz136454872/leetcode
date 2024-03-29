from typing import List


# Offer 47 礼物的最大价值
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        log = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]

        for i in range(len(grid)):
            log[i][0] = grid[i][0] + (log[i - 1][0] if i > 0 else 0)

        for j in range(len(grid[0])):
            log[0][j] = grid[0][j] + (log[0][j - 1] if j > 0 else 0)

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                log[i][j] = max(log[i - 1][j], log[i][j - 1]) + grid[i][j]

        return log[-1][-1]


inp = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(Solution().maxValue(inp))


# 有界数组中指定下标处的最大值
class Solution2:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def count(v):
            out = v
            left_len = min(v, index + 1)
            left_height = max(1, v - index)
            left_area = (left_height + v) * left_len // 2
            # print('left',left_area)
            right_len = max(0, min(v - 1, n - index - 1))
            right_height = max(1, v - (n - index - 1))
            right_area = (right_height + v - 1) * right_len // 2
            # print('right',right_area)

            return left_area + right_area

        # print('total',count(0))
        maxSum -= n
        l = 0
        r = 10**9 + 1

        while l <= r:
            mid = (l + r) // 2

            if count(mid) <= maxSum:
                l = mid + 1
            else:
                r = mid - 1

        return l


# 插入后的最大值
class Solution3:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] == '-':
            i = 1

            while i < len(n) and int(n[i]) <= x:
                i += 1

            return n[:i] + str(x) + n[i:]
        i = 0

        while i < len(n) and int(n[i]) >= x:
            i += 1

        return n[:i] + str(x) + n[i:]


# sl = Solution()
# # grid=[[1,2,5],[3,2,1]]
# n = 4
# index = 0
# maxSum = 4
# n = "-132"
# x = 3
# print(sl.maxValue(n, x))
