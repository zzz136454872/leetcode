from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        ox = defaultdict(list)
        oy = defaultdict(list)

        for o in obstacles:
            ox[o[0]].append(o[1])
            oy[o[1]].append(o[0])

        for v in ox.values():
            v.sort()

        for v in oy.values():
            v.sort()
        loc = [0, 0]
        d = (0, 1)
        dirs = [{
            (0, 1): (-1, 0),
            (-1, 0): (0, -1),
            (0, -1): (1, 0),
            (1, 0): (0, 1)
        }, {
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1)
        }]

        res = 0

        for c in commands:
            if c < 0:
                d = dirs[c][d]
                print(loc, d)

                continue

            if d[0] == 0:

                nloc = [loc[0], loc[1] + d[1] * c]
                os = ox[loc[0]]

                if d[1] > 0:
                    l1 = bisect_right(os, loc[1])

                    if l1 < len(os) and os[l1] <= nloc[1]:
                        loc[1] = os[l1] - 1
                    else:
                        loc[1] = nloc[1]
                else:
                    l1 = bisect_left(os, loc[1])
                    l1 -= 1

                    if l1 >= 0 and os[l1] >= nloc[1]:
                        loc[1] = os[l1] + 1
                    else:
                        loc[1] = nloc[1]
            else:
                nloc = [loc[0] + c * d[0], loc[1]]
                os = oy[loc[1]]

                if d[0] > 0:
                    l1 = bisect_right(os, loc[0])

                    if l1 < len(os) and os[l1] <= nloc[0]:
                        loc[0] = os[l1] - 1
                    else:
                        loc[0] = nloc[0]
                else:
                    l1 = bisect_left(os, loc[0])
                    l1 -= 1

                    if l1 >= 0 and os[l1] >= nloc[0]:
                        loc[0] = os[l1] + 1
                    else:
                        loc[0] = nloc[0]
            res = max(res, loc[0]**2 + loc[1]**2)
            print(loc, d)

        return res


commands = [4, -1, 3]
obstacles = []
commands = [4, -1, 4, -2, 4]
obstacles = [[2, 4]]
commands = [-2, -1, -2, 3, 7]
obstacles = [[1, -3], [2, -3], [4, 0], [-2, 5], [-5, 2], [4, -4], [-2, -5],
             [-1, -2], [0, 2], [0, 0]]
print(Solution().robotSim(commands, obstacles))
