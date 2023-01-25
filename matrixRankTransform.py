from typing import List


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        parent = {}

        def find(a):
            if a in parent:
                return find(parent[a])

            return a

        def union(a, b):
            a = find(a)
            b = find(b)

            if a != b:
                parent[max(a, b)] = min(a, b)

        rank = {}
        adj = {}

        for i in range(len(matrix)):
            tmp = sorted([(matrix[i][j], i, j) for j in range(len(matrix[0]))])

            for j in range(1, len(matrix[0])):
                if tmp[j][0] == tmp[j - 1][0]:
                    union(tmp[j - 1][1:], tmp[j][1:])

        for j in range(len(matrix[0])):
            tmp = sorted([(matrix[i][j], i, j) for i in range(len(matrix))])

            for i in range(1, len(matrix)):
                if tmp[i][0] == tmp[i - 1][0]:
                    union(tmp[i - 1][1:], tmp[i][1:])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                t = find((i, j))

                if t not in adj:
                    adj[t] = set()

        for i in range(len(matrix)):
            tmp = sorted([(matrix[i][j], i, j) for j in range(len(matrix[0]))])

            for j in range(1, len(matrix[0])):
                t1 = find(tmp[j - 1][1:])
                t2 = find(tmp[j][1:])

                if t1 != t2:
                    adj[t1].add(t2)

        for j in range(len(matrix[0])):
            tmp = sorted([(matrix[i][j], i, j) for i in range(len(matrix))])

            for i in range(1, len(matrix)):
                if tmp[i][0] == tmp[i - 1][0]:
                    union(tmp[i - 1][1:], tmp[i][1:])
                else:
                    t1 = find(tmp[i - 1][1:])
                    t2 = find(tmp[i][1:])

                    if t1 != t2:
                        adj[t1].add(t2)

        inbound = {}

        for p1 in adj:
            for p2 in adj[p1]:
                if p2 not in inbound:
                    inbound[p2] = 0
                inbound[p2] += 1

        queue = []

        for p1 in adj:
            if p1 not in inbound:
                queue.append(p1)

        number = 1
        rank = {}

        while len(queue) > 0:
            newqueue = []

            while len(queue) > 0:
                now = queue.pop()
                rank[now] = number

                for nxt in adj[now]:
                    inbound[nxt] -= 1

                    if inbound[nxt] == 0:
                        newqueue.append(nxt)
            number += 1
            queue = newqueue

        return [[rank[find((i, j))] for j in range(len(matrix[0]))]
                for i in range(len(matrix))]


matrix = [[1, 2], [3, 4]]
matrix = [[7, 7], [7, 7]]
matrix = [[20, -21, 14], [-19, 4, 19], [22, -47, 24], [-19, 4, 19]]
matrix = [[7, 3, 6], [1, 4, 5], [9, 8, 2]]

print(Solution().matrixRankTransform(matrix))
