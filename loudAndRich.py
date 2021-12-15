from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]],
                    quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for i in range(n)]

        for r in richer:
            graph[r[1]].append(r[0])

        mem = [-1 for i in range(n)]

        def search(idx):
            if mem[idx] != -1:
                return mem[idx]
            out = idx

            for nidx in graph[idx]:
                tmp = search(nidx)

                if quiet[out] > quiet[tmp]:
                    out = tmp
            mem[idx] = out

            return out

        for i in range(n):
            search(i)

        return mem


richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
quiet = [3, 2, 5, 4, 6, 1, 7, 0]
# richer = []
# quiet = [0]
print(Solution().loudAndRich(richer, quiet))
