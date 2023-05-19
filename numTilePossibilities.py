from collections import Counter
from functools import cache


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        c = tuple(Counter(tiles).values())

        @cache
        def find(a):
            res = 1

            for i in range(len(a)):
                if a[i] == 0:
                    break

                na = list(a)
                na[i] -= 1
                res += find(tuple(sorted(na, reverse=True)))

            return res

        return find(c) - 1


tiles = "AAB"
tiles = "AAABBC"
tiles = "V"
print(Solution().numTilePossibilities(tiles))
