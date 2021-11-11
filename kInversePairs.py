class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mem = [[-1] * (k + 1) for i in range(n + 1)]
        mod = 10**9 + 7

        def find(n, k):
            if k < 0:
                return 0

            if mem[n][k] != -1:
                return mem[n][k]

            if n <= 1:
                out = 1 if k == 0 else 0
                mem[n][k] = out

                return out

            if k == 0:
                mem[n][k] = 1

                return 1
            out = (find(n - 1, k) + find(n, k - 1) - find(n - 1, k - n)) % mod
            mem[n][k] = out

            return out

        return find(n, k)


n = 3
k = 0
n = 3
k = 1
k = 2
n = 2
print(Solution().kInversePairs(n, k))
