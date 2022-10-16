from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        group = [[] for i in range(n + 1)]

        for a, b in dislikes:
            group[b].append(a)
            group[a].append(b)
        flag = [0 for i in range(n + 1)]

        def dye(i, f):
            flag[i] = f

            for j in group[i]:
                if flag[j] == 0:
                    if not dye(j, 3 - f):
                        return False
                elif flag[j] != 3 - f:
                    return False

            return True

        for i in range(n):
            if flag[i] != 0:
                continue

            if not dye(i, 0):
                return False

        return True


n = 4
dislikes = [[1, 2], [1, 3], [2, 4]]
n = 3
dislikes = [[1, 2], [1, 3], [2, 3]]
n = 5
dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
# n=10
# dislikes=[[1,2],[3,4],[5,6],[6,7],[8,9],[7,8]]
print(Solution().possibleBipartition(n, dislikes))
