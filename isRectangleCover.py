from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        def area(rec):
            return (rec[3] - rec[1]) * (rec[2] - rec[0])

        nodes = {}
        totalArea = 0

        for rec in rectangles:
            nodes[(rec[0], rec[1])] = nodes.get((rec[0], rec[1]), 0) + 1
            nodes[(rec[2], rec[3])] = nodes.get((rec[2], rec[3]), 0) + 1
            nodes[(rec[0], rec[3])] = nodes.get((rec[0], rec[3]), 0) + 1
            nodes[(rec[2], rec[1])] = nodes.get((rec[2], rec[1]), 0) + 1
            totalArea += area(rec)
        vertexs = []
        print('flag')
        print(nodes)

        for node in nodes.keys():
            if nodes[node] == 1:
                vertexs.append(node)
            elif nodes[node] == 2 or nodes[node] == 4:
                continue
            else:
                return False
        print('flag1')

        if len(vertexs) != 4:
            return False
        vertexs.sort()

        if vertexs[0][0] != vertexs[1][0] or vertexs[2][0] != vertexs[3][
                0] or vertexs[0][1] != vertexs[2][1] or vertexs[1][
                    1] != vertexs[3][1]:
            return False

        return area(vertexs[0] + vertexs[3]) == totalArea


rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4],
              [2, 3, 3, 4]]
rectangles = [[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]
rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [3, 2, 4, 4]]
rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]]
print(Solution().isRectangleCover(rectangles))
