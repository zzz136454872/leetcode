class Solution:
    def numTilings(self, n: int) -> int:
        f0 = 0
        f1 = 0
        f2 = 0
        f3 = 1
        mod = 10**9 + 7

        for i in range(n):
            nf0 = f3
            nf1 = (f0 + f2) % mod
            nf2 = (f0 + f1) % mod
            nf3 = (f0 + f1 + f2 + f3) % mod
            f0 = nf0
            f1 = nf1
            f2 = nf2
            f3 = nf3

        return f3


n = 3
n = 4
n = 5
print(Solution().numTilings(n))

# # # # # #
# # # # # #
# # ##
# ## #
