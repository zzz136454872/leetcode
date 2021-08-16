class Solution:
    def countArrangement(self, n: int) -> int:
        log = [True for i in range(n + 1)]
        candidates = [[] for i in range(n)]

        for i in range(n):
            for j in range(1, n + 1):
                if (i + 1) % j == 0 or j % (i + 1) == 0:
                    candidates[i].append(j)
        # print(candidates)

        def find(level):
            if level == n:
                return 1
            out = 0

            for num in candidates[level]:
                if log[num]:
                    log[num] = False
                    out += find(level + 1)
                    log[num] = True

            return out

        return find(0)


sl = Solution()
n = 2
print(sl.countArrangement(2))
