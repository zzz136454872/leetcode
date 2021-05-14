from typing import List

mod = 10**9 + 7


def c(i, k):
    out = 1

    for i in range(i):
        out = out * (k - i) // (i + 1)

    return out % mod


# 不知道是哪个题
class Solution1:
    def numWays(self, s: str) -> int:
        cn = s.count('1')

        if cn % 3 != 0:
            return 0

        if cn == 0:
            return c(2, len(s) - 1)
        cn = cn // 3
        i = 0
        j = len(s) - 1
        ci = 0
        cj = 0

        while ci < cn:
            if s[i] == '1':
                ci += 1
            i += 1

        while cj < cn:
            if s[j] == '1':
                cj += 1
            j -= 1
        ii = i
        jj = j
        # print(ii,jj,i,j)

        while s[ii] != '1':
            ii += 1

        while s[jj] != '1':
            jj -= 1

        return ((ii - i + 1) * (j - jj + 1)) % mod

# tle
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod=10**9+7
        mem=[[-1]*(steps+1) for i in range(arrLen)]
        def dp(pos,step):
            if step<0:
                return 0
            if pos>=arrLen:
                return 0
            if pos<0:
                return 0
            if pos>step:
                return 0
            if pos==step:
                return 1
            if mem[pos][step]!=-1:
                return mem[pos][step]
            out=(dp(pos+1,step-1)+dp(pos,step-1)+dp(pos-1,step-1))%mod
            mem[pos][step]=out
            return out
        return dp(0,steps)

sl = Solution()
s = "100100010100110"
steps=438
arrLen=315977
print(sl.numWays(steps, arrLen))
print('done')
