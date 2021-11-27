from typing import List


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        stack = []
        j = 0
        out = -12345678901234

        for i in range(len(points) - 1):
            while j < len(points) and points[j][0] - points[i][0] <= k:
                tmp = points[j][0] + points[j][1]

                while len(stack) > 0 and stack[-1] < tmp:
                    stack.pop()
                stack.append(tmp)
                j += 1

            if points[i][1] + points[i][0] == stack[0]:
                stack.pop(0)

            if len(stack) > 0:
                out = max(out, stack[0] + points[i][1] - points[i][0])
            # print(i,j,stack,out)

        return out


points = [[1, 3], [2, 0], [5, 10], [6, -10]]
k = 1
points = [[0, 0], [3, 0], [9, 2]]
k = 3
points = [[-19, 9], [-15, -19], [-5, -8]]
k = 10
print(Solution().findMaxValueOfEquation(points, k))
