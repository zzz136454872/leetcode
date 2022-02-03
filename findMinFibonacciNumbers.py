class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k == 0:
            return 0

        if k == 1:
            return 1
        a = 1
        b = 1

        while a <= k:
            a, b = a + b, a

        return self.findMinFibonacciNumbers(k - b) + 1


k = 7
k = 10
k = 19
print(Solution().findMinFibonacciNumbers(k))
