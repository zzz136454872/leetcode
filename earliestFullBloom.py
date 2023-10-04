from collections import defaultdict
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]],
                         people: List[int]) -> List[int]:
        mem = defaultdict(int)

        for f in flowers:
            mem[f[0]] += 1
            mem[f[1] + 1] -= 1
        mem2 = sorted(mem.items())
        ps = sorted([[people[i], i, 0] for i in range(len(people))])
        j = 0
        tmp = 0

        for i in range(len(ps)):
            while j < len(mem2) and mem2[j][0] <= ps[i][0]:
                tmp += mem2[j][1]
                j += 1
            ps[i][2] = tmp
        ps.sort(key=lambda x: x[1])

        return [x[2] for x in ps]


flowers = [[1, 6], [3, 7], [9, 12], [4, 13]]
people = [2, 3, 7, 11]
print(Solution().fullBloomFlowers(flowers, people))
