class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        kk = (k + 1) // 2
        r = (k + 1) % 2
        a = self.kthGrammar(n - 1, kk)

        if a == 0:
            if r == 0:
                return 0

            return 1
        else:
            if r == 1:
                return 0

            return 1


n = 1
k = 1
n = 2
k = 1
n = 2
k = 2
n = 3
k = 3
print(Solution().kthGrammar(n, k))
