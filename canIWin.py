from typing import List


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False

        mem = dict()

        def dfs(remain, target):
            tr = tuple(remain)

            if (tr, target) in mem:
                return mem[(tr, target)]

            if max(remain) >= target:
                return True

            res = False

            for num in remain:
                nr = remain.copy()
                nr.remove(num)

                if not dfs(nr, target - num):
                    res = True

                    break
            mem[(tr, target)] = res

            return res

        return dfs(list(i + 1 for i in range(maxChoosableInteger)),
                   desiredTotal)


print(Solution().canIWin(19, 190))
