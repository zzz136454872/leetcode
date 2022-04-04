from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        mem = {}
        win = set()

        for match in matches:
            win.add(match[0])
            mem[match[1]] = mem.get(match[1], 0) + 1
        l0 = []
        l1 = []

        for w in win:
            if w not in mem:
                l0.append(w)

        for w in mem:
            if mem[w] == 1:
                l1.append(w)

        return [sorted(l0), sorted(l1)]


matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9],
           [10, 4], [10, 9]]
print(Solution().findWinners(matches))
