from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        k = 1234567
        m = 112347
        t = 1
        i = 0
        j = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while True:
            t = (t * k) % m
            idx = t % 4
            flag = True

            for n in range(4):
                ni = i + dirs[(n+idx)%4][0]
                nj = j + dirs[(n+idx)%4][1]

                if ni < 0 or ni >= len(mat) or nj < 0 or nj >= len(mat[0]):
                    continue

                if mat[ni][nj] > mat[i][j]:
                    print('from', i, j, 'to', ni, nj)
                    flag = False
                    i = ni
                    j = nj

                    break

            if flag:
                return (i, j)

        return (-1, -1)


mat = [[1, 4], [3, 2]]
mat = [[10, 20, 15], [21, 30, 14], [7, 16, 32]]
print(Solution().findPeakGrid(mat))
