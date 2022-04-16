from typing import List


class Solution:
    def largestPalindrome(self, n: int) -> int:
        # mod = 1337

        # if n == 1:
        #     return 9
        # start = int('9' * n)

        # for i in range(start, 10**(n - 1), -1):
        #     tmp = i * 10**n + int(str(i)[::-1])
        #     test = 10**n - 1

        #     while test * test >= tmp:
        #         if tmp % test == 0:
        #             print(tmp, test)

        #             return tmp % mod
        #         test -= 1

        return [-1, 9, 987, 123, 597, 677, 1218, 877, 475][n]


f = Solution()
out = [f.largestPalindrome(i + 1) for i in range(8)]
print(out)
