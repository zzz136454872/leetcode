from typing import List


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mem = {}
        mod = 10**9 + 7

        def find(nn, l):
            if (nn, l) in mem:
                return mem[nn, l]

            if l == 0:
                if nn == 0:
                    return 1

                return 0

            out = find(nn - 1, l - 1) * (n - nn + 1)
            out += find(nn, l - 1) * max(nn - k, 0)

            out %= mod
            mem[(nn, l)] = out

            return out

        return find(n, goal)


N = 3
L = 3
K = 1
N = 2
L = 3
K = 0
print(Solution().numMusicPlaylists(N, L, K))
