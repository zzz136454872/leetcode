from functools import cache


class Solution:
    def countVowelStrings(self, n: int) -> int:
        @cache
        def find(a, k):
            if k == 1:
                return 1

            if a == 0:
                return 0
            res = 1

            for i in range(a):
                res += find(a - i, k - 1)

            return res

        return find(n, 5)


n = 1
n = 2
n = 33
print(Solution().countVowelStrings(n))
