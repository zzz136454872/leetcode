class Solution:
    def soupServings(self, n: int) -> float:
        n = (n + 24) // 25
        mem = {}

        # if n>200:
        #     return 1
        def find(a, b):
            if a <= 0 or b <= 0:
                if a <= 0 and b <= 0:
                    return 0.5

                if a <= 0:
                    return 1

                return 0

            if (a, b) in mem:
                return mem[a, b]
            tmp = 0.25 * (find(a - 4, b) + find(a - 3, b - 1) +
                          find(a - 2, b - 2) + find(a - 1, b - 3))
            mem[(a, b)] = tmp

            return tmp

        return find(n, n)


n = 100
n = 50
print(Solution().soupServings(n))
