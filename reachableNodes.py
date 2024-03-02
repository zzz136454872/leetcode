from collections import defaultdict, deque
from heapq import heappop, heappush
from typing import List


# 不知道是哪个
class Solution1:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int,
                       n: int) -> int:
        link = defaultdict(lambda: {})
        maxd = 10**9
        distance = [maxd] * n

        for edge in edges:
            link[edge[0]][edge[1]] = [edge[2] + 1, 0]
            link[edge[1]][edge[0]] = [edge[2] + 1, 0]
        heap = [(0, 0)]
        i = 0
        prevd = 0

        while len(heap) > 0:
            d, p = heappop(heap)

            if d >= distance[p]:
                continue
            i += 1
            # print('d=',d,'p=',p,'i=',i)
            distance[p] = d

            for nxt, rlink in link[p].items():
                if rlink[0] + d <= maxMoves:
                    heappush(heap, (rlink[0] + d, nxt))
                    rlink[1] = rlink[0] - 1
                else:
                    rlink[1] = max(rlink[1], maxMoves - distance[p])
            prevd = d
        res = 0

        for d in distance:
            if d < maxd:
                res += 1

        for p1 in link:
            for p2 in link[p1]:
                if p1 > p2:
                    continue
                res += min(link[p1][p2][0] - 1,
                           link[p1][p2][1] + link[p2][p1][1])

        return res


# edges = [[0, 1, 10], [0, 2, 1], [1, 2, 2]]
# maxMoves = 6
# n = 3
# edges = [[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]]
# maxMoves = 10
# n = 4
# edges = [[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]]
# maxMoves = 17
# n = 5
# print(Solution().reachableNodes(edges, maxMoves, n))


# 2368. 受限条件下可到达节点的数目
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]],
                       restricted: List[int]) -> int:
        link = [[] for i in range(n)]
        r = set(restricted)

        for s, t in edges:
            if s in r or t in r:
                continue
            link[s].append(t)
            link[t].append(s)

        q = deque([(-1, 0)])
        res = 1

        while len(q) > 0:
            from_, now = q.popleft()

            for nxt in link[now]:
                if nxt == from_:
                    continue
                res += 1
                q.append((now, nxt))

        return res


n = 7
edges = [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]]
restricted = [4, 5]
n = 7
edges = [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]]
restricted = [4, 2, 1]

print(Solution().reachableNodes(n, edges, restricted))
