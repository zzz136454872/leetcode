from typing import List


class Solution:
    def countSubgraphsForEachDiameter(self, n: int,
                                      edges: List[List[int]]) -> List[int]:
        res = [0] * n
        adjList = [[] for i in range(n)]

        for edge in edges:
            s = edge[0] - 1
            e = edge[1] - 1
            adjList[e].append(s)
            adjList[s].append(e)

        def isTree(nodes):
            if len(nodes) <= 1:
                return len(nodes) == 1
            sn = set(nodes)
            visited = {n: False for n in nodes}
            queue = [nodes[0]]

            while len(queue) > 0:
                now = queue.pop()
                visited[now] = True

                for nxt in adjList[now]:
                    if nxt in sn and not visited[nxt]:
                        queue.append(nxt)

            return all(visited.values())

        def getDistance(nodes):
            if len(nodes) <= 2:
                return len(nodes) - 1
            sn = set(nodes)

            dis = 1

            for node in nodes:
                distance = {n: -1 for n in nodes}
                queue = [node]
                distance[node] = 0

                while len(queue) > 0:
                    now = queue.pop()

                    for nxt in adjList[now]:
                        if nxt in sn and distance[nxt] == -1:
                            queue.append(nxt)
                            distance[nxt] = distance[now] + 1
                dis = max(dis, max(distance.values()))

            return dis

        for i in range(2**n):
            nodes = []

            for j in range(n):
                if i & (2**j) != 0:
                    nodes.append(j)

            if isTree(nodes):
                d = getDistance(nodes)
                res[d] += 1

        return res[1:]


n = 4
edges = [[1, 2], [2, 3], [2, 4]]
n = 2
edges = [[1, 2]]
n = 3
edges = [[1, 2], [2, 3]]
print(Solution().countSubgraphsForEachDiameter(n, edges))
