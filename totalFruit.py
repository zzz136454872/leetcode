from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        r = 0
        mem = {}
        res = 0

        for l in range(len(fruits)):
            if fruits[l] not in mem:
                mem[fruits[l]] = 1

                while len(mem.keys()) > 2:
                    mem[fruits[r]] -= 1

                    if mem[fruits[r]] == 0:
                        del mem[fruits[r]]
                    r += 1
            else:
                mem[fruits[l]] += 1
            res = max(res, l - r + 1)

        return res


fruits = [1, 2, 1]
fruits = [0, 1, 2, 2]
fruits = [1, 2, 3, 2, 2]
print(Solution().totalFruit(fruits))
