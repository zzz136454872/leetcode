from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        nor = set()
        noc = set()

        for i in range(len(mat)):
            ctr = 0

            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    ctr += 1

                    if ctr > 1:
                        nor.add(i)

        for j in range(len(mat[0])):
            ctr = 0

            for i in range(len(mat)):
                if mat[i][j] == 1:
                    ctr += 1

                    if ctr > 1:
                        noc.add(j)

        res = 0

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and i not in nor and j not in noc:
                    res += 1

        return res


mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
mat = [[0, 1, 0], [0, 0, 0], [1, 0, 0], [1, 0, 0]]
print(Solution().numSpecial(mat))
