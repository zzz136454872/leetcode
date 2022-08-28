from typing import *


def count(n):
    out = 0

    while n > 0:
        n = n // 5
        out += n

    return out


def find(K):
    start = 0
    end = 5 * K

    while start <= end:
        mid = (start + end) // 2
        n = count(mid)

        if n < K:
            start = mid + 1
        else:
            end = mid - 1

    return start


class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        return find(K + 1) - find(K)


sl = Solution()
print(sl.preimageSizeFZF(5))
