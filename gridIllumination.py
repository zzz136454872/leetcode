from collections import defaultdict
from typing import List


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]],
                         queries: List[List[int]]) -> List[int]:
        memx = defaultdict(lambda: set())
        memy = defaultdict(lambda: set())
        meme = defaultdict(lambda: set())
        mems = defaultdict(lambda: set())
        memt = set()

        for lamp in lamps:
            tmp = (lamp[0], lamp[1])
            memx[lamp[0]].add(tmp)
            memy[lamp[1]].add(tmp)
            meme[lamp[0] - lamp[1]].add(tmp)
            mems[lamp[0] + lamp[1]].add(tmp)
            memt.add(tmp)

        out = []

        def close(x, y):
            memt.remove((x, y))
            memx[x].discard((x, y))

            if len(memx[x]) == 0:
                del memx[x]
            memy[y].discard((x, y))

            if len(memy[y]) == 0:
                del memy[y]
            meme[x - y].discard((x, y))

            if len(meme[x - y]) == 0:
                del meme[x - y]
            mems[x + y].discard((x, y))

            if len(mems[x + y]) == 0:
                del mems[x + y]

        for q in queries:

            if q[0] in memx or q[
                    1] in memy or q[0] - q[1] in meme or q[0] + q[1] in mems:
                out.append(1)
            else:
                out.append(0)
            tests = [(q[0] - 1, q[1] - 1), (q[0] - 1, q[1]),
                     (q[0] - 1, q[1] + 1), (q[0], q[1] - 1), (q[0], q[1]),
                     (q[0], q[1] + 1), (q[0] + 1, q[1] - 1), (q[0] + 1, q[1]),
                     (q[0] + 1, q[1] + 1)]

            for t in tests:
                if t in memt:
                    close(*t)

        return out


n = 5
lamps = [[0, 0], [4, 4]]
queries = [[1, 1], [1, 0]]

n = 5
lamps = [[0, 0], [4, 4]]
queries = [[1, 1], [1, 1]]

n = 5
lamps = [[0, 0], [0, 4]]
queries = [[0, 4], [0, 1], [1, 4]]
print(Solution().gridIllumination(n, lamps, queries))
