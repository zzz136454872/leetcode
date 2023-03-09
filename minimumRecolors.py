class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = 0

        for i in range(k):
            if blocks[i] == 'W':
                n += 1
        res = n

        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                n += 1

            if blocks[i - k] == 'W':
                n -= 1
            res = min(res, n)

        return res


blocks = "WBBWWBBWBW"
k = 7
blocks = "WBWBBBW"
k = 2
print(Solution().minimumRecolors(blocks, k))
