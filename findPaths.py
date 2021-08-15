class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int,
                  startColumn: int) -> int:
        mod = 10**9 + 7
        mem = [[[-1] * (maxMove + 1) for j in range(n + 1)]
               for i in range(m + 1)]

        def dp(r, c, move):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1

            if move == 0:
                return 0

            if mem[r][c][move] != -1:
                return mem[r][c][move]
            tmp = (dp(r, c - 1, move - 1) + dp(r, c + 1, move - 1) +
                   dp(r - 1, c, move - 1) + dp(r + 1, c, move - 1)) % mod
            mem[r][c][move] = tmp

            return tmp

        return dp(startRow, startColumn, maxMove)



sl = Solution()
m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0
print(sl.findPaths(m, n, maxMove, startRow, startColumn))
