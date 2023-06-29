from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int,
                          colsum: List[int]) -> List[List[int]]:
        b = []

        if upper + lower != sum(colsum):
            return []
        c = colsum.count(2)
        upper -= c
        lower -= c

        if upper < 0 or lower < 0:
            return []
        tmp = [1 if a == 2 else 0 for a in colsum]
        res = [tmp.copy(), tmp]

        for i in range(len(colsum)):
            if colsum[i] == 1:
                if upper > lower:
                    res[0][i] = 1
                    upper -= 1
                else:
                    res[1][i] = 1
                    lower -= 1

        return res


upper = 2
lower = 1
colsum = [1, 1, 1]
upper = 2
lower = 3
colsum = [2, 2, 1, 1]
upper = 5
lower = 5
colsum = [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]
# upper=9
# lower=2
# colsum=[0,1,2,0,0,0,0,0,2,1,2,1,2]

# [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
# [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1]
print(Solution().reconstructMatrix(upper, lower, colsum))
