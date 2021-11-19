class Solution:
    def integerReplacement(self, n: int) -> int:
        mem = {}

        def find(n):
            if n == 1:
                return 0

            if n in mem.keys():
                return mem[n]

            if n % 2 == 0:
                return find(n // 2) + 1

            return min(find((n + 1) // 2), find((n - 1) // 2)) + 2

        return find(n)


n = 8
n = 7
n = 4
print(Solution().integerReplacement(n))
