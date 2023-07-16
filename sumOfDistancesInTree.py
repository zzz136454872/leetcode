from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int,
                             edges: List[List[int]]) -> List[int]:
        if N == 0:
            return []

        if len(edges) == 0:
            return [0]
        distance = [0 for i in range(N)]
        count = [1 for i in range(N)]
        neighbor = [[] for i in range(N)]

        for edge in edges:
            neighbor[edge[0]].append(edge[1])
            neighbor[edge[1]].append(edge[0])

        def getRootDistance(child, parent):
            for c in neighbor[child]:
                if c != parent:
                    getRootDistance(c, child)
                    count[child] += count[c]
                    distance[child] += count[c] + distance[c]

        def shiftRoot(child, parent):
            for c in neighbor[child]:
                if c != parent:
                    distance[c] = distance[child] - 2 * count[c] + N
                    shiftRoot(c, child)

        getRootDistance(0, -1)
        #print(distance)
        #print(count)
        #print(neighbor)
        shiftRoot(0, -1)

        return distance


sl = Solution()
N = 6
edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
print(sl.sumOfDistancesInTree(N, edges))
