from collections import defaultdict
from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int],
                              numWanted: int, useLimit: int) -> int:
        mem = defaultdict(int)
        a = [(values[i], labels[i]) for i in range(len(values))]
        a.sort(key=lambda x: -x[0])
        res = 0
        count = 0

        for i in range(len(a)):
            if mem[a[i][1]] < useLimit:
                mem[a[i][1]] += 1
                res += a[i][0]
                count += 1

                if count == numWanted:
                    break

        return res


values = [5, 4, 3, 2, 1]
labels = [1, 1, 2, 2, 3]
numWanted = 3
useLimit = 1
values = [5, 4, 3, 2, 1]
labels = [1, 3, 3, 3, 2]
numWanted = 3
useLimit = 2
values = [9, 8, 8, 7, 6]
labels = [0, 0, 0, 1, 1]
numWanted = 3
useLimit = 1
print(Solution().largestValsFromLabels(values, labels, numWanted, useLimit))
