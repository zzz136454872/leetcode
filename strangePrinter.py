class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        table = [[-1] * n for i in range(n)]

        def count(start, end):
            if start > end:
                return 0

            if start == end:
                return 1

            if table[start][end] != -1:
                return table[start][end]

            if s[start] == s[end]:
                tmp = count(start, end - 1)
            else:
                tmp = 101

                for i in range(start, end):
                    tmp = min(tmp, count(start, i) + count(i + 1, end))
            table[start][end] = tmp

            return tmp

        return count(0, n - 1)


sl = Solution()
s = "aba"
print(sl.strangePrinter(s))
