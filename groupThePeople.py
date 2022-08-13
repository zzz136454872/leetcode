from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mem = {}

        for i in range(len(groupSizes)):
            if groupSizes[i] in mem:
                mem[groupSizes[i]].append(i)
            else:
                mem[groupSizes[i]] = [i]

        res = []

        for k in mem:
            for i in range(len(mem[k]) // k):
                res.append(mem[k][i * k:(i + 1) * k])

        return res


groupSizes = [3, 3, 3, 3, 3, 1, 3]
groupSizes = [2, 1, 3, 3, 3, 2]
print(Solution().groupThePeople(groupSizes))
