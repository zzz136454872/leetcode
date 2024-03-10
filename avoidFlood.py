from bisect import bisect_right
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        tmp = []
        mem = {}
        res = [-1] * len(rains)

        for i in range(len(rains)):
            if rains[i] == 0:
                tmp.append(i)
            elif rains[i] not in mem:
                mem[rains[i]] = i
            else:
                loc = bisect_right(tmp, mem[rains[i]])

                if loc == len(tmp):
                    return []
                res[tmp[loc]] = rains[i]
                del tmp[loc]
                mem[rains[i]] = i

        for v in tmp:
            res[v] = 1

        return res


rains = [1, 2, 3, 4]
rains = [1, 2, 0, 0, 2, 1]
rains = [1, 2, 0, 1, 2]
print(Solution().avoidFlood(rains))
