from typing import *


# 解码方法
class Solution1:
    def numDecodings(self, s: str) -> int:
        log = [0] * (len(s) + 1)
        log[0] = 1

        if s[0] == '0':
            return 0
        else:
            log[1] = 1
        table = {str(i) for i in range(1, 27)}

        for i in range(1, len(s)):
            if s[i] in table:
                log[i + 1] = log[i]

            if s[i - 1:i + 1] in table:
                log[i + 1] += log[i - 1]
        # print(log)

        return log[-1]


# 解码方法II
class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10**9 + 7
        n = len(s)
        mem = [0] * (n + 1)
        mem[0] = 1
        log = {'**': 15, '1*': 9, '2*': 6}
        table = {str(i) for i in range(1, 27)}

        if s[0] == '0':
            return 0
        elif s[0] == '*':
            mem[1] = 9
        else:
            mem[1] = 1

        for i in range(1, n):
            if s[i] == '*':
                if s[i - 1:i + 1] in log:
                    mem[i + 1] = (log[s[i - 1:i + 1]] * mem[i - 1]) % mod
                mem[i + 1] = (mem[i + 1] + 9 * mem[i]) % mod
            elif s[i - 1] == '*':
                if s[i] < '7':
                    mem[i + 1] = (2 * mem[i - 1]) % mod
                else:
                    mem[i + 1] = (1 * mem[i - 1]) % mod

                if s[i] != '0':
                    mem[i + 1] = (mem[i + 1] + mem[i]) % mod
            else:
                if s[i] in table:
                    mem[i + 1] = mem[i]

                if s[i - 1:i + 1] in table:
                    mem[i + 1] = (mem[i + 1] + mem[i - 1]) % mod
        print(mem)

        return mem[-1]


sl = Solution()
s = "12"
s = "*"
s = "1*"
s = "2*"
s = "**"
s = "*1"
print(sl.numDecodings(s))
