class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def sub(a):
            if a == 1:
                return 0

            return (k + sub(a - 1)) % a

        return sub(n) + 1


print(Solution().findTheWinner(n, k))
