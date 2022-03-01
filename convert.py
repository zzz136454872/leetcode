class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)

        if n == 1 or numRows == 1:
            return s

        mem = [[0] * n for i in range(numRows)]
        p = 0
        direction = 0
        i = -1
        j = 0

        while p < n:
            if direction == 0:
                if i == numRows - 1:
                    j += 1
                    i -= 1
                    direction = 1
                else:
                    i += 1
            else:
                if i == 0:
                    i += 1
                    direction = 0
                else:
                    i -= 1
                    j += 1
            mem[i][j] = s[p]
            p += 1
        out = []

        for i in range(numRows):
            for j in range(n):
                if mem[i][j]:
                    out.append(mem[i][j])

        return ''.join(out)


s = "PAYPALISHIRING"
numRows = 3
s = "PAYPALISHIRING"
numRows = 4
s = "A"
numRows = 1
s = "AB"
numRows = 2
print(Solution().convert(s, numRows))
