class Solution:
    def champagneTower(self, poured: int, query_row: int,
                       query_glass: int) -> float:
        mem = [[poured]]

        for i in range(query_row + 1):
            tmp = [0]

            for j in range(i + 1):
                a = max(0, (mem[i][j] - 1) / 2)
                tmp[-1] += a
                tmp.append(a)
            mem.append(tmp)

        return min(1, mem[query_row][query_glass])


poured = 1
query_glass = 1
query_row = 1
poured = 2
query_glass = 1
query_row = 1
print(Solution().champagneTower(poured, query_row, query_glass))
