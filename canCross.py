from typing import *


class Solution:
    def canCross(self, stones: List[int]) -> bool:

        log = {s: set() for s in stones}

        if 0 not in log.keys() or 1 not in log.keys():
            return False
        log[0].add(0)
        target = stones[-1]

        for s in stones:
            for v in log[s]:
                if v > 1 and s + v - 1 in log.keys():
                    log[s + v - 1].add(v - 1)

                if v > 0 and s + v in log.keys():
                    log[s + v].add(v)

                if s + v + 1 in log.keys():
                    log[s + v + 1].add(v + 1)

            if log[target]:
                return True

        return False


sl = Solution()
stones = [0, 1, 2, 3, 4, 8, 9, 11]
print(sl.canCross(stones))
