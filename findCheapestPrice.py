from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int,
                          dst: int, k: int) -> int:
        mem = [[] for i in range(n)]

        for flight in flights:
            mem[flight[0]].append((flight[1], flight[2]))
        inf = 123456789
        dis = [inf for i in range(n)]
        dis[src] = 0
        queue = [src]
        jump = 0

        while jump <= k and len(queue) > 0:
            queue2 = []
            # print(jump,queue,dis)
            new_dis = dis.copy()

            while len(queue) > 0:
                now = queue.pop()

                for pd in mem[now]:
                    if dis[now] + pd[1] < new_dis[pd[0]]:
                        new_dis[pd[0]] = dis[now] + pd[1]
                        queue2.append(pd[0])
            queue = queue2
            dis = new_dis
            jump += 1
            # print(dis)

        if dis[dst] != inf:
            return dis[dst]

        return -1


sl = Solution()
n = 3
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
k = 1
k = 0

n = 5
edges = [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]]
src = 0
dst = 2
k = 2
print(sl.findCheapestPrice(n, edges, src, dst, k))
