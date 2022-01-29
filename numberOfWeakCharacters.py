from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort()
        mem = [[properties[0][1]]]
        last = properties[0][0]

        for i in range(1, len(properties)):
            if properties[i][0] > last:
                mem.append([properties[i][1]])
            else:
                mem[-1].append(properties[i][1])
            last = properties[i][0]

        nmax = [0 for i in range(len(mem))]

        for i in range(len(mem) - 2, -1, -1):
            nmax[i] = max(nmax[i + 1], max(mem[i + 1]))

        out = 0

        for i in range(len(mem)):
            for defence in mem[i]:
                if defence < nmax[i]:
                    out += 1

        return out


properties = [[5, 5], [6, 3], [3, 6]]
properties = [[2, 2], [3, 3]]
properties = [[1, 5], [10, 4], [4, 3]]
print(Solution().numberOfWeakCharacters(properties))
