from typing import List


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        mem = [[0] * i for i in range(n)]

        def find(start, end):
            if start > end:
                return 0

            if start == end:
                return 1

            if mem[end][start] > 0:
                return mem[end][start]

            if s[start] == s[end]:
                return 2 + find(start + 1, end - 1)
            tmp = max(find(start, end - 1), find(start + 1, end))
            mem[end][start] = tmp

            return tmp

        return find(0, n - 1)


sl = Solution()
s = "bbbab"
s = 'abcccbac'
# s = "cbbd"
print(sl.longestPalindromeSubseq(s))
